-- SELECT actors.fi 

-- UNION

SELECT first_name, last_name FROM actors
UNION
SELECT movie_title, movie_story FROM movies
ORDER BY first_name
-- it has to be the same amount of COLUMNS for UNION DOES NOT 
-- DISPLAY duplicated rows
-- use join when you need to combine data from related tables when 
-- when there is data with foreign key