-- FOREIGN KEY: PARENT AND CHILD TABLES
-- THE TABLE THAT HAS THE FK IS CHILD 
-- THE TABLE WITH THE CANDIDATE KEY IS THE PARENT

-- LET'S CREATE A CHILD TABLE TO OUR ACTORS TABLE

-- CREATE TABLE movies(
-- movie_id SERIAL,
-- movie_title VARCHAR(100) NOT NULL,
-- movie_story TEXT,
-- actor_playing_id INTEGER,
-- PRIMARY KEY (movie_id),
-- FOREIGN KEY (actor_playing_id) REFERENCES actors(actor_id))
-- -- SELECT * FROM movies

-- INSERT INTO movies (movie_title, movie_story, actor_playing_id)
-- VALUES ('Good Will Hunting', 'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
-- 		(SELECT actor_id FROM actors WHERE first_name = 'Matt' AND last_name = 'Damon'));

-- INSERT INTO movies (movie_title, movie_story, actor_playing_id)
-- VALUES ('Troya', 'Movie about the legendary war of Troya', 
--     (SELECT actor_id from actors WHERE first_name='Brad' AND last_name='Pitt'));

SELECT * FROM movies
