-- -- Part I
-- -- Part I.1
-- CREATE TABLE customer (
--     customer_number SERIAL PRIMARY KEY,
--     first_name VARCHAR(50) NOT NULL,
--     last_name VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE customer_profile (
--     customer_id INT PRIMARY KEY, 
--     isLoggedIn BOOLEAN DEFAULT FALSE, 
--     CONSTRAINT fk_customer
--         FOREIGN KEY (customer_id) REFERENCES Customer(customer_number) ON DELETE CASCADE
-- -- );

-- -- -- Part I.2
-- INSERT INTO customer (first_name, last_name)
-- VALUES 
--     ('John', 'Doe'),
--     ('Jerome', 'Lalu'),
--     ('Lea', 'Rive');
	
-- SELECT * FROM customer
-- -- Part I.3

-- INSERT INTO customerprofile (customer_id, isLoggedIn)
-- VALUES (
--     (SELECT customer_number FROM Customer WHERE first_name = 'John' AND last_name = 'Doe'),
--     TRUE
-- );

-- INSERT INTO customerprofile (customer_id, isLoggedIn)
-- VALUES (
--     (SELECT customer_number FROM Customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'),
--     FALSE
-- );

-- SELECT * FROM customerprofile
-- Part I.4

-- The first_name of the LoggedIn customers
-- SELECT customer.first_name
-- FROM customer 
-- INNER JOIN customerprofile  ON customer.customer_number = customerprofile.customer_id
-- WHERE customerprofile.isLoggedIn = TRUE;

-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.

-- SELECT customer.first_name, customerprofile.isLoggedIn
-- FROM customer 
-- LEFT JOIN customerprofile ON customer.customer_number = customerprofile.customer_id;

-- The number of customers that are not LoggedIn

-- SELECT COUNT(*)
-- FROM customer 
-- LEFT JOIN customerprofile ON customer.customer_number = customerprofile.customer_id
-- WHERE customerprofile.isLoggedIn IS NULL OR customerprofile.isLoggedIn = FALSE;



