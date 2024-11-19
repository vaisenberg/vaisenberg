--AGREGATE FUNCTIONS

-- SELECT * FROM actors

-- SELECT AVG(oscars) AS avg_oscars FROM actors;

-- SELECT COUNT(first_name) AS total_actors from actors

-- SELECT * FROM actors

-- SELECT SUM(oscars) AS gm_oscars FROM actors WHERE first_name = 'George'

-- SELECT first_name, last_name, max(oscars) FROM actors GROUP BY first_name, last_name;
-- INSERT INTO actors (first_name, last_name, age, oscars)
-- VALUES('Matt','Ross','03/01/1970', 0);

-- SELECT DISTINCT first_name FROM actors order by first_name DESC

-- SELECT * FROM actors WHERE first_name not in ('George', 'Brad')

-- SELECT * FROM actors

-- SELECT * FROM actors WHERE age BETWEEN '1960-01-01' AND '1971-01-01'

SELECT *
FROM actors 
WHERE oscars = (SELECT MAX(oscars) FROM actors)


