-- 	Exercise 1 : Items and customers
-- CREATE TABLE items (
-- items_id SERIAL PRIMARY KEY,
-- item VARCHAR(50) NOT NULL,
-- item_price NUMERIC(10) NOT NULL
-- )
-- SELECT * FROM items
-- INSERT INTO items(item, item_price)
-- VALUES('Small Desk', 100);
-- INSERT INTO items(item, item_price)
-- VALUES('Large Desk', 300);
-- INSERT INTO items(item, item_price)
-- VALUES('Fan', 80);
-- SELECT * FROM items
-- CREATE TABLE customers (
-- customer_id SERIAL PRIMARY KEY,
-- customer_name VARCHAR(20),
-- customer_surname VARCHAR(50)
-- )
-- SELECT * FROM customers
-- INSERT INTO customers(customer_name,customer_surname)
-- VALUES('Greg', 'Jones'),
-- ('Sandra','Jones'),
-- ('Scott','Scott'),
-- ('Trevor','Trevor'),
-- ('Melanie','Johnson')
-- SELECT * FROM customers
-- Use SQL to fetch the following data from the database:
-- All the items.
-- SELECT * FROM items
-- Use SQL to fetch the following data from the database:
-- All the items with a price above 80 (80 not included).
-- SELECT * FROM items WHERE item_price > 80
-- Use SQL to fetch the following data from the database:
-- All the items with a price below 300. (300 included)
-- SELECT * FROM items WHERE item_price < 300
-- All customers whose last name is ‘Smith’ (What will be your outcome?).
-- SELECT * FROM customers WHERE customer_surname = 'Smith' - 
-- it will show no record, just primary keys
-- All customers whose last name is ‘Jones’:
-- SELECT * FROM customers WHERE customer_surname = 'Jones'
-- All customers whose firstname is not ‘Scott’:
-- SELECT * FROM customers WHERE customer_surname != 'Scott'











