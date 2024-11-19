-- SQL JOINS: INNER, LEFT, RIGHT, FULL

--INNER JOIN SYNTAX

-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- INNER JOIN movies
-- ON actors.actor_id = movies.actor_playing_id

-- CREATE TABLE producers(
-- producer_id SERIAL,
-- producer_name VARCHAR(100) NOT NULL,
-- producer_lastname VARCHAR(100) NOT NULL,
-- movie_producer_id INTEGER,
-- PRIMARY KEY (producer_id),
-- FOREIGN KEY (movie_producer_id) REFERENCES movies(movie_id)


-- INSERT INTO producers (producer_name, producer_lastname, movie_producer_id) 
-- VALUES ('Lawrence', 'Bender',(SELECT movie_id from movies WHERE movie_title = 'Good Will Hunting')),
-- 	   ('Wolfgang', 'Petersen',(SELECT movie_id from movies WHERE movie_title = 'Troya'))

-- SELECT * FROM producers

-- SELECT producers.producer_name, producers.producer_lastname, movies.movie_title
-- FROM movies
-- LEFT JOIN producers
-- ON producers.movie_producer_id = movies.movie_id

-- LEFT JOIN:
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- LEFT JOIN movies
-- ON actors.actor_id = movies.actor_playing_id

--RIGHT JOIN
-- SELECT producers.producer_name, producers.producer_lastname, movies.movie_title
-- FROM movies
-- RIGHT JOIN producers
-- ON producers.movie_producer_id = movies.movie_id

--FULL JOIN
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- FULL JOIN movies
-- ON actors.actor_id = movies.actor_playing_id

-- CREATE TABLE countries (
-- 	country_id SERIAL PRIMARY KEY,
-- country_name VARCHAR(50) NOT NULL)

-- INSERT INTO countries (country_name)
-- VALUES ('Peru')

-- SELECT actors.first_name, countries.country_name
-- FROM actors
-- INNER JOIN countries
-- ON actors.actor_id = countries.country_id








