-- Exercise 1: Movie Rankings and Analysis(combined_db_movies)
-- Task 1: Rank Movies by Popularity within Each Genre

SELECT
    g.genre_name,
    m.title AS movie_title,
    m.popularity,
    RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS popularity_rank
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
    g.genre_name, popularity_rank;
-------------------------------------------
-- Task 2: Identify the Top 3 Movies by Revenue within Each Production Company
SELECT
    pc.company_name,
    m.title AS movie_title,
    m.revenue,
    NTILE(4) OVER (PARTITION BY pc.company_name ORDER BY m.revenue DESC) AS revenue_quartile
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
ORDER BY
    pc.company_name, revenue_quartile;
-----------------------------------------------
-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre
SELECT
    g.genre_name,
    m.title AS movie_title,
    m.budget,
    SUM(m.budget) OVER (
        PARTITION BY g.genre_name
        ORDER BY m.budget DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total_budget
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
    g.genre_name, m.budget DESC;
------------------------------------------------------------	
-- Task 4: Identify the Most Recent Movie for Each Genre
SELECT DISTINCT
    g.genre_name,
    FIRST_VALUE(m.title) OVER (
        PARTITION BY g.genre_name
        ORDER BY m.release_date DESC
    ) AS most_recent_movie,
    FIRST_VALUE(m.release_date) OVER (
        PARTITION BY g.genre_name
        ORDER BY m.release_date DESC
    ) AS most_recent_release_date
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
    g.genre_name;
-------------------------------------------
-- Exercise 2: Cast and Crew Performance Analysis

-- Task 1: Rank Actors by Their Appearance in Movies
SELECT
    p.person_name AS actor_name,
    COUNT(mc.movie_id) AS movie_count,
    DENSE_RANK() OVER (
        ORDER BY COUNT(mc.movie_id) DESC
    ) AS rank
FROM
    movies.movie_cast mc
JOIN
    movies.person p
ON
    mc.person_id = p.person_id
GROUP BY
    p.person_name
ORDER BY
    rank;
--------------------------------------------
-- Task 2: Identify the Top Director by Average Movie Rating
SELECT
    d.person_name AS director_name,
    AVG(m.vote_average) AS avg_rating
FROM
    movies.movie_crew mc
JOIN
    movies.movie m
ON
    mc.movie_id = m.movie_id
JOIN
    movies.person d
ON
    mc.person_id = d.person_id
WHERE
    mc.job = 'Director'
GROUP BY
    d.person_name
ORDER BY
    avg_rating DESC
LIMIT 1;
----------------------------------------------------------------
-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor

SELECT
    p.person_name AS actor_name,
    SUM(m.revenue) AS cumulative_revenue
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
GROUP BY
    p.person_name
ORDER BY
    cumulative_revenue DESC;
-------------------------------------------------------------------
-- Task 4: Identify the Director Whose Movies Have the Highest Total Budget
WITH director_budgets AS (
    SELECT
        p.person_name AS director_name,
        SUM(m.budget) AS total_budget
    FROM
        movies.movie_crew mc
    JOIN
        movies.movie m
    ON
        mc.movie_id = m.movie_id
    JOIN
        movies.person p
    ON
        mc.person_id = p.person_id
    WHERE
        mc.job = 'Director' 
    GROUP BY
        p.person_name
)
SELECT
    director_name,
    total_budget
FROM
    (
        SELECT
            director_name,
            total_budget,
            RANK() OVER (ORDER BY total_budget DESC) AS rank
        FROM
            director_budgets
    ) ranked_directors
WHERE
    rank = 1;
