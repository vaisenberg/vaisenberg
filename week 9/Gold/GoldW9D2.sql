-- Exerceise 1.1
WITH movie_budgets AS (
    SELECT
        m.title AS movie_title,
        m.release_date,
        m.budget,
        LAG(m.budget) OVER (ORDER BY m.release_date ASC) AS previous_budget,
        LEAD(m.budget) OVER (ORDER BY m.release_date ASC) AS next_budget
    FROM
        movies.movie m
)
SELECT
    movie_title,
    release_date,
    budget,
    previous_budget,
    next_budget
FROM
    movie_budgets
WHERE
    previous_budget < budget
    AND next_budget < budget
ORDER BY
    release_date;
--------------------------------------------
-- Exercise 1.2
WITH genre_ratings AS (
    SELECT
        g.genre_name,
        m.title AS movie_title,
        EXTRACT(YEAR FROM m.release_date) AS release_year,
        m.vote_average
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
)
SELECT
    genre_name,
    movie_title,
    release_year,
    AVG(vote_average) OVER (
        PARTITION BY genre_name
        ORDER BY release_year ASC
        RANGE BETWEEN 5 PRECEDING AND CURRENT ROW
    ) AS moving_avg_rating
FROM
    genre_ratings
ORDER BY
    genre_name, release_year;
-----------------------------------------------
-- Exercise 1.3
SELECT
    g.genre_name,
    m.title AS movie_title,
    m.revenue,
    ROW_NUMBER() OVER (
        PARTITION BY g.genre_name
        ORDER BY m.revenue DESC
    ) AS row_number,
    RANK() OVER (
        PARTITION BY g.genre_name
        ORDER BY m.revenue DESC
    ) AS rank,
    DENSE_RANK() OVER (
        PARTITION BY g.genre_name
        ORDER BY m.revenue DESC
    ) AS dense_rank
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
    g.genre_name, revenue DESC;
----------------------------------------------------
-- Exercise 2.1
WITH actor_movies AS (
    SELECT
        p.person_name AS actor_name,
        m.title AS movie_title,
        m.release_date,
        FIRST_VALUE(m.title) OVER (
            PARTITION BY p.person_name
            ORDER BY m.release_date ASC
        ) AS first_movie_title,
        FIRST_VALUE(m.release_date) OVER (
            PARTITION BY p.person_name
            ORDER BY m.release_date ASC
        ) AS first_movie_release_date,
        LAST_VALUE(m.title) OVER (
            PARTITION BY p.person_name
            ORDER BY m.release_date ASC
            ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
        ) AS last_movie_title,
        LAST_VALUE(m.release_date) OVER (
            PARTITION BY p.person_name
            ORDER BY m.release_date ASC
            ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
        ) AS last_movie_release_date
    FROM
        movies.movie_cast mc
    JOIN
        movies.person p
    ON
        mc.person_id = p.person_id
    JOIN
        movies.movie m
    ON
        mc.movie_id = m.movie_id
)
SELECT DISTINCT
    actor_name,
    first_movie_title,
    first_movie_release_date,
    last_movie_title,
    last_movie_release_date
FROM
    actor_movies
ORDER BY
    actor_name;
---------------------------------------------
-- Exercise 2.2
WITH genre_avg_revenue AS (
   
    SELECT
        g.genre_name,
        AVG(m.revenue) AS avg_genre_revenue
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
    GROUP BY
        g.genre_name
),
above_avg_genres AS (

    SELECT
        genre_name
    FROM
        genre_avg_revenue
    WHERE
        avg_genre_revenue > (SELECT AVG(revenue) FROM movies.movie)
)

SELECT
    g.genre_name,
    m.title AS movie_title,
    m.revenue,
    RANK() OVER (
        PARTITION BY g.genre_name
        ORDER BY m.popularity DESC
    ) AS popularity_rank
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
WHERE
    g.genre_name IN (SELECT genre_name FROM above_avg_genres)
ORDER BY
    g.genre_name, popularity_rank;
------------------------------------------------------
-- Exercise 2.3
WITH movie_revenue_percentile AS (

    SELECT
        m.movie_id,
        m.title AS movie_title,
        m.revenue,
        PERCENT_RANK() OVER (ORDER BY m.revenue DESC) AS revenue_percentile
    FROM
        movies.movie m
),
top_10_percent_movies AS (
   
    SELECT
        movie_id,
        revenue
    FROM
        movie_revenue_percentile
    WHERE
        revenue_percentile <= 0.1
),
actor_revenue AS (
   
    SELECT
        p.person_name AS actor_name,
        SUM(m.revenue) AS total_revenue
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
    WHERE
        m.movie_id IN (SELECT movie_id FROM top_10_percent_movies)
    GROUP BY
        p.person_name
)

SELECT
    actor_name,
    total_revenue
FROM
    actor_revenue
ORDER BY
    total_revenue DESC;


