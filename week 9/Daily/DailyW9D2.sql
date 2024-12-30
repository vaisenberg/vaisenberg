-- Task 1: Calculate the Average Budget Growth Rate for Each Production Company

WITH budget_growth AS (
    SELECT
        pc.company_name,
        m.title AS movie_title,
        m.budget,
        LAG(m.budget) OVER (
            PARTITION BY pc.company_name 
            ORDER BY m.release_date ASC
        ) AS previous_budget,
        CASE
            WHEN LAG(m.budget) OVER (
                PARTITION BY pc.company_name 
                ORDER BY m.release_date ASC
            ) > 0 THEN
                (m.budget - LAG(m.budget) OVER (
                    PARTITION BY pc.company_name 
                    ORDER BY m.release_date ASC
                ))::FLOAT / LAG(m.budget) OVER (
                    PARTITION BY pc.company_name 
                    ORDER BY m.release_date ASC
                ) * 100
            ELSE NULL
        END AS growth_rate
    FROM
        movies.movie_company mc
    JOIN
        movies.production_company pc
    ON
        mc.company_id = pc.company_id
    JOIN
        movies.movie m
    ON
        mc.movie_id = m.movie_id
)
SELECT
    company_name,
    AVG(growth_rate) AS average_growth_rate
FROM
    budget_growth
WHERE
    growth_rate IS NOT NULL -- Exclude rows where growth rate couldn't be calculated
GROUP BY
    company_name
ORDER BY
    average_growth_rate DESC;
------------------------------------------------------
-- Task 2: Determine the Most Consistently High-Rated Actor

WITH average_movie_rating AS (
    SELECT
        AVG(m.vote_average) AS avg_rating
    FROM
        movies.movie m
),

high_rated_appearances AS (
    SELECT
        p.person_name AS actor_name,
        COUNT(mc.movie_id) AS high_rated_movie_count
    FROM
        movies.movie_cast mc
    JOIN
        movies.movie m
    ON
        mc.movie_id = m.movie_id
    JOIN
        movies.person p
    ON
        mc.person_id = p.person_id
    CROSS JOIN
        average_movie_rating
    WHERE
        m.vote_average > average_movie_rating.avg_rating
    GROUP BY
        p.person_name
)

SELECT
    actor_name,
    high_rated_movie_count
FROM
    high_rated_appearances
ORDER BY
    high_rated_movie_count DESC
LIMIT 1;
-----------------------------------------------------------
-- Task 3: Calculate the Rolling Average Revenue for Each Genre
SELECT
    g.genre_name,
    m.title AS movie_title,
    m.revenue,
    AVG(m.revenue) OVER (
        PARTITION BY g.genre_name
        ORDER BY m.release_date ASC
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_revenue
FROM
    movies.movie_genres mg
JOIN
    movies.genre g
ON
    mg.genre_id = g.genre_id
JOIN
    movies.movie m
ON
    mg.movie_id = m.movie_id
ORDER BY
    g.genre_name, m.release_date ASC;
-------------------------------------------------------------
--  Task 4: Identify the Highest-Grossing Movie Series
WITH series_revenue AS (
    SELECT
        k.keyword_name AS series_name,
        SUM(m.revenue) AS total_revenue
    FROM
        movies.movie_keywords mk
    JOIN
        movies.keyword k
    ON
        mk.keyword_id = k.keyword_id
    JOIN
        movies.movie m
    ON
        mk.movie_id = m.movie_id
    GROUP BY
        k.keyword_name
),
ranked_series AS (
    SELECT
        series_name,
        total_revenue,
        RANK() OVER (ORDER BY total_revenue DESC) AS rank
    FROM
        series_revenue
)
SELECT
    series_name,
    total_revenue
FROM
    ranked_series
WHERE
    rank = 1;


