CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10, 2)
);

CREATE TABLE sales_data (
    sale_id INT PRIMARY KEY,
    employee_id INT,
    sales DECIMAL(10, 2),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
------------------------------------------------------------
INSERT INTO employees (employee_id, first_name, last_name, department_id, salary) VALUES
(1, 'John', 'Doe', 1, 60000),
(2, 'Jane', 'Smith', 2, 80000),
(3, 'Jim', 'Brown', 3, 90000),
(4, 'Jake', 'White', 4, 70000),
(5, 'Jill', 'Green', 5, 75000),
(6, 'Jack', 'Black', 3, 95000),
(7, 'Jerry', 'Gray', 2, 82000);

INSERT INTO sales_data (sale_id, employee_id, sales) VALUES
(1, 1, 1000),
(2, 2, 1500),
(3, 3, 2000),
(4, 4, 700),
(5, 5, 1300),
(6, 6, 1750),
(7, 7, 1200);
-------------------------------------------------------------
SELECT e.employee_id, e.first_name, e.last_name, e.department_id, s.sales,
       RANK() OVER (PARTITION BY e.department_id ORDER BY s.sales DESC) AS sales_rank,
       DENSE_RANK() OVER (PARTITION BY e.department_id ORDER BY s.sales DESC) AS dense_sales_rank
FROM employees e
JOIN sales_data s ON e.employee_id = s.employee_id;
---------------------------------------------------------------
SELECT employee_id, first_name, last_name, department_id, salary,
       NTILE(4) OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_quartile
FROM employees;
----------------------------------------------------------------
SELECT e.employee_id, e.first_name, e.last_name, e.department_id, s.sales,
       SUM(s.sales) OVER (PARTITION BY e.department_id ORDER BY e.employee_id) AS running_total
FROM employees e
JOIN sales_data s ON e.employee_id = s.employee_id;
---------------------------------------------------------------
-- Exercise 1: Employee Salaries
-- Task 1
SELECT 
    department_id,
    first_name || ' ' || last_name AS employee_name,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_rank
FROM 
    employees
ORDER BY 
    department_id, salary_rank;
-----------------------------------------------------------------	
-- Task 2
SELECT 
    department_id,
    first_name || ' ' || last_name AS employee_name,
    salary,
    SUM(salary) OVER (PARTITION BY department_id ORDER BY salary DESC) AS cumulative_salary
FROM 
    employees
ORDER BY 
    department_id, salary DESC;
--------------------------------------------------------------------
-- Exercise 2: Sales Performance
-- Task 1
SELECT
    e.department_id,
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    s.sales,
    DENSE_RANK() OVER (PARTITION BY e.department_id ORDER BY s.sales DESC) AS sales_rank
FROM
    employees e
JOIN
    sales_data s
ON
    e.employee_id = s.employee_id
ORDER BY
    e.department_id, sales_rank;
---------------------------------------------
-- Task 2
SELECT
    e.employee_id,
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    s.sales,
    SUM(s.sales) OVER () AS total_sales_all_employees,
    SUM(s.sales) OVER (ORDER BY s.sales DESC) AS running_total_sales
FROM
    employees e
JOIN
    sales_data s
ON
    e.employee_id = s.employee_id
ORDER BY
    running_total_sales;



