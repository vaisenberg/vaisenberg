-- PART II
-- 1.
-- CREATE TABLE book (
-- book_id SERIAL PRIMARY KEY,  
-- title VARCHAR(255) NOT NULL, 
-- author VARCHAR(255) NOT NULL 
-- );

-- 2.
-- INSERT INTO book (title, author)
-- VALUES 
--     ('Alice in Wonderland', 'Lewis Carroll'),
--     ('Harry Potter', 'J.K. Rowling'),
--     ('To Kill a Mockingbird', 'Harper Lee');

-- 3.
-- CREATE TABLE student (
-- student_id SERIAL PRIMARY KEY, 
-- name VARCHAR(255) NOT NULL UNIQUE,
-- age INT CHECK (age <= 15)
-- )

-- 4.
-- INSERT INTO student (name, age) 
-- VALUES 
--     ('John', 12),
--     ('Lera', 11),
--     ('Patrick', 10),
--     ('Bob', 14);
-- SELECT * FROM student

-- 5.
-- CREATE TABLE library (
-- book_fk_id INT,
-- student_fk_id INT,
-- borrowed_date DATE,
-- PRIMARY KEY (book_fk_id, student_fk_id),  
-- FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,  
-- FOREIGN KEY (student_fk_id) REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE  
-- );

-- SELECT * FROM library
-- 6.
-- INSERT INTO library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES
--     ((SELECT book_id FROM book WHERE title = 'Alice in Wonderland' AND author = 'Lewis Carroll'), 
--      (SELECT student_id FROM student WHERE name = 'John'), '2022-02-15'),

--     ((SELECT book_id FROM book WHERE title = 'To Kill a Mockingbird' AND author = 'Harper Lee'), 
--      (SELECT student_id FROM student WHERE name = 'Bob'), '2021-03-03'),

--     ((SELECT book_id FROM book WHERE title = 'Alice in Wonderland' AND author = 'Lewis Carroll'), 
--      (SELECT student_id FROM student WHERE name = 'Lera'), '2021-05-23'),

--     ((SELECT book_id FROM book WHERE title = 'Harry Potter' AND author = 'J.K. Rowling'), 
--      (SELECT student_id FROM student WHERE name = 'Bob'), '2021-08-12');
-- 7.
-- SELECT book.title AS book_title, 
--        book.author AS book_author, 
--        student.name AS student_name, 
--        library.borrowed_date
-- FROM library 
-- JOIN book  ON library.book_fk_id = book.book_id
-- JOIN student ON library.student_fk_id = student.student_id;

-- SELECT student.name AS student_name, 
--        book.title AS book_title
-- FROM library 
-- JOIN Book ON library.book_fk_id = book.book_id
-- JOIN student ON library.student_fk_id = student.student_id;

-- SELECT AVG(student.age) AS average_age
-- FROM library 
-- JOIN book  ON library.book_fk_id = book.book_id
-- JOIN student  ON library.student_fk_id = student.student_id
-- WHERE book.title = 'Alice in Wonderland';

-- DELETE FROM student WHERE student_id = 1;
-- Deleting a student will automatically remove all their borrowing records in the Library table.


