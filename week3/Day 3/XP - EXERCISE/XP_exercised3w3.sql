--EXERCISE 1
-- 1.Get a list of all the languages, from the language table.
-- SELECT name from language

-- 2.Get a list of all films joined with their languages – select the following details : film title, description, and language name.
-- SELECT film.title AS film_title, film.description AS film_description,language.name AS language_name FROM film
-- JOIN language ON film.language_id = language.language_id;

-- 3.Get all languages, even if there are no films in those languages – select the following details 
-- : film title, description, and language name.
-- SELECT film.title AS film_title, film.description AS film_description,language.name AS language_name FROM film
-- RIGHT JOIN language ON film.language_id = language.language_id;

-- 4.Create a new table called new_film with the following columns : id, name. Add some new films to the table.
-- CREATE TABLE new_film(
-- id_new_film SERIAL PRIMARY KEY,
-- name VARCHAR(100) NOT NULL 
-- )
-- INSERT INTO new_film (name)
-- VALUES
-- ('Feather Christmas'),('The Merry Gentlemen'),('Chosen Family')

-- 5.Customer review
-- CREATE TABLE customer_review (
-- review_id SERIAL PRIMARY KEY,
-- film_id INT NOT NULL,                   
-- language_id INT NOT NULL,                
-- title_review VARCHAR(255) NOT NULL,            
-- score INT NOT NULL CHECK (score BETWEEN 1 AND 10),
-- review_text TEXT,                     
-- last_update DATE,
-- FOREIGN KEY (language_id) REFERENCES language(language_id),
-- FOREIGN KEY (film_id) REFERENCES new_film(id_new_film))
-- SELECT * FROM customer_review

-- 6.
-- INSERT INTO customer_review (film_id, language_id, title_review, score, review_text, last_update)
-- VALUES
-- (1, 1, 'Fantastic Movie!', 9, 'This film was an amazing experience, highly recommend it!', '2024-11-19'),
-- (2, 1, 'Could Be Better', 6, 'The story was okay, but the visuals were stunning.', '2024-11-18');
-- 7.ERROR:delete on table "new_film" violates foreign key constraint "customer_review_film_id_fkey" on table "customer_review"
-- DELETE FROM new_film
-- WHERE name = 'Feather Christmas'

-- EXERCISE 2
-- 1. Changing the language for the first 3 films

-- UPDATE film
-- SET language_id = 2
-- WHERE film_id IN (1,2,3) 
-- SELECT * FROM film WHERE language_id =2

-- 2. it has 3 FOREIGN KEYS: customer_address_id_fkey - reference to table address, payment_customer_id_fkey reference to table payment
-- and rental_customer_id_fkey reference to table rental in order INSERT into the customer table You must first insert records 
-- into the referenced tables

-- 3. NO NEED TO CHECK
-- DROP TABLE customer_review

-- 4.Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
-- SELECT COUNT(return_date IS NULL) FROM rental

-- 5.Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)

-- SELECT film.film_id AS film_id, 
--        film.title AS film_title, 
--        film.rental_rate AS price
-- FROM film
-- JOIN inventory ON film.film_id = inventory.film_id
-- JOIN rental ON inventory.inventory_id = rental.inventory_id
-- WHERE rental.return_date IS NULL
-- ORDER BY film.rental_rate DESC, film.film_id ASC
-- LIMIT 30;

-- 6.1The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
-- SELECT film.title AS title, 
--        film.description AS description
-- FROM film
-- WHERE film.film_id IN (
--     SELECT film_actor.film_id
--     FROM film_actor
--     WHERE film_actor.actor_id IN (
--         SELECT actor.actor_id
--         FROM actor
--         WHERE actor.first_name = 'Penelope'
--           AND actor.last_name = 'Monroe'
--     )
-- )
-- AND film.description iLIKE '%sumo%';
-- 6.2The 2nd film : A short documentary (less than 1 hour long), rated “R”.

-- SELECT * FROM category - documentary category_id = 6 reference to film_id

-- SELECT film.title AS title, 
--        film.length AS length, 
--        film.rating AS rating
-- FROM film
-- WHERE film.film_id IN (
--     SELECT film_category.film_id
--     FROM film_category
--     WHERE film_category.category_id = 6
-- )
-- AND film.rating = 'R' 
-- AND film.length < 60;

-- 6.3  film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, 
-- and he returned it between the 28th of July and the 1st of August, 2005.

-- SELECT film.title AS title,
--        film.film_id AS id_title,
--        film.rental_rate AS rental_rate
-- FROM film
-- WHERE film.film_id IN (
--     SELECT inventory.film_id
--     FROM inventory
--     WHERE inventory.inventory_id IN (
--         SELECT rental.inventory_id
--         FROM rental
--         WHERE rental.customer_id = (
--             SELECT customer.customer_id
--             FROM customer
--             WHERE customer.first_name = 'Matthew' 
--               AND customer.last_name = 'Mahan'
--         )
--         AND rental.rental_id IN (
--             SELECT payment.rental_id
--             FROM payment
--             WHERE payment.amount > 4
--         )
--         AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01'
--     )
-- );

-- 6.4His friend Matthew Mahan watched this film, as well. 
-- It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace

-- SELECT film.title,
--        film.replacement_cost
-- FROM film
-- ORDER BY film.replacement_cost DESC;
--we will set expensive DVD > 17.99

-- SELECT film.title AS title,
--        film.film_id AS id_title,
--        film.replacement_cost AS rp
-- FROM film
-- WHERE film.film_id IN (
--     SELECT inventory.film_id
--     FROM inventory
--     WHERE inventory.inventory_id IN (
--         SELECT rental.inventory_id
--         FROM rental
--         WHERE rental.customer_id = (
--             SELECT customer.customer_id
--             FROM customer
--             WHERE customer.first_name = 'Matthew' 
--               AND customer.last_name = 'Mahan'
--         )
--     )
-- )
-- AND film.description ILIKE '%boat%'
-- AND film.replacement_cost > 17.99;


