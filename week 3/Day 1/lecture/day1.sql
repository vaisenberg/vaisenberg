--  CREATE TABLE actors (
-- actor_id SERIAL PRIMARY KEY,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(50) NOT NULL,
-- age DATE NOT NULL,
-- number_oscars SMALLINT NOT NULL)

-- SELECT * FROM actors

-- INSERT INTO actors (first_name, last_name, age,number_oscars)
-- VALUES ('Matt', 'Damon', '08/10/1970', 5);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('George','Clooney','06/05/1961', 2);

-- SELECT * FROM actors

-- INSERT INTO actors (first_name, last_name, age,number_oscars)
-- VALUES ('Brad', 'Pitt', '08/10/1970', 3)

-- SELECT * FROM actors WHERE number_oscars > 2 AND first_name = 'Brad'

-- SELECT first_name, last_name FROM actors WHERE first_name = 'Matt'  OR  
-- number_oscars = 2 ;

-- SELECT last_name FROM actors WHERE last_name ILIKE 'c%' LIMIT 2

-- SELECT ACTOR_ID FROM actors WHERE last_name ILIKE 'c%' OFFSET 3

-- SELECT first_name, last_name FROM actors WHERE number_oscars > 2 
-- ORDER BY number_oscars DESC;

-- UPDATE actors 
-- SET first_name = 'Angelina',
-- last_name = 'Jolie'
-- WHERE first_name = 'George';

-- SELECT * FROM actors

-- DELETE FROM actors 
-- Where actor_id = 1

-- INSERT INTO actors (first_name, last_name, age,number_oscars)
-- VALUES ('Angelina', 'Jolie', '08/10/1970', 3)

-- TRUNCATE TABLE actors RESTART IDENTITY

-- INSERT INTO actors (first_name, last_name, age,number_oscars)
-- VALUES ('Angelina', 'Jolie', '08/10/1970', 3);

-- SELECT * FROM actors

-- ALTER TABLE actors RENAME number_oscars TO oscars

-- DROP TABLE IF EXISTS actors;
-- SELECT * FROM actors
