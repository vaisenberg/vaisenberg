-- Create the employees table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date VARCHAR(20),
    department VARCHAR(50)
);
--------------------------------
-- Insert 20 sample records 
INSERT INTO employees (employee_id, employee_name, salary, hire_date, department) VALUES
(1, 'Amy West', 60000.00, '2021-01-15', 'HR'),
(2, 'Ivy Lee', 75000.50, '2020-05-22', 'Sales'),
(3, 'joe smith', 80000.75, '2019-08-10', 'Marketing'), 
(4, 'John White', 90000.00, '2020-11-05', 'Finance'),
(5, 'Jane Hill', 55000.25, '2022-02-28', 'IT'),
(6, 'Dave West', 72000.00, '2020-03-12', 'Marketing'),
(7, 'Fanny Lee', 85000.50, '2018-06-25', 'Sales'),
(8, 'Amy Smith', 95000.25, '2019-11-30', 'Finance'),
(9, 'Ivy Hill', 62000.75, '2021-07-18', 'IT'),
(10, 'Joe White', 78000.00, '2022-04-05', 'Marketing'),
(11, 'John Lee', 68000.50, '2018-12-10', 'HR'),
(12, 'Jane West', 89000.25, '2017-09-15', 'Sales'),
(13, 'Dave Smith', 60000.75, '2022-01-08', NULL),
(14, 'Fanny White', 72000.00, '2019-04-22', 'IT'),
(15, 'Amy Hill', 84000.50, '2020-08-17', 'Marketing'),
(16, 'Ivy West', 92000.25, '2021-02-03', 'Finance'),
(17, 'Joe Lee', 58000.75, '2018-05-28', 'IT'),
(18, 'John Smith', 77000.00, '2019-10-10', 'HR'),
(19, 'Jane Hill', 81000.50, '2022-03-15', 'Sales'),
(20, 'Dave White', 70000.25, '2017-12-20', 'Marketing');
--------------------------------------------------------------


-- 1.Identify and handle any missing value.

SELECT 
    COUNT(*) AS total_rows,
    COUNT(employee_id) AS employee_id_not_null,
    COUNT(employee_name) AS employee_name_not_null,
    COUNT(salary) AS salary_not_null,
    COUNT(hire_date) AS hire_date_not_null,
    COUNT(department) AS department_not_null
FROM employees;

SELECT *
FROM employees
WHERE employee_id IS NULL 
   OR employee_name IS NULL 
   OR salary IS NULL 
   OR hire_date IS NULL 
   OR department IS NULL;

UPDATE employees
SET department = 'Unknown'
WHERE department IS NULL;

-----------------------------------------------------------------
-- 2. Check for and eliminate any duplicate rows in the dataset.
SELECT 
    employee_id, 
    employee_name, 
    salary, 
    hire_date, 
    department,
    COUNT(*) AS duplicate_count
FROM employees
GROUP BY 
    employee_id, 
    employee_name, 
    salary, 
    hire_date, 
    department
HAVING COUNT(*) > 1;
--------------------------------------------------------------------

-- 3. Correct any structural issues, such as inconsistent naming conventions or formatting errors.
UPDATE employees
SET employee_name = INITCAP(employee_name);

UPDATE employees
SET department = INITCAP(department)
WHERE department IS NOT NULL;

UPDATE employees
SET employee_name = TRIM(employee_name),
    department = TRIM(department);

UPDATE employees
SET department = 'Unknown'
WHERE department IS NULL;

ALTER TABLE employees
RENAME COLUMN hire_date TO hireDate;

-------------------------------------------------------------------------------
--4. Ensure all columns have appropriate data types (e.g. the hire_date column).

SELECT * FROM employees

ALTER TABLE employees
ALTER COLUMN salary TYPE NUMERIC(10, 2);

ALTER TABLE employees
ALTER COLUMN hireDate TYPE DATE USING hireDate::DATE;

SELECT DISTINCT department
FROM employees;

UPDATE employees
SET department = 'HR'
WHERE department = 'Hr';
---------------------------------------------------------------------------------
-- 5. Detect and address any outliers that may skew the analysis.
WITH salary_stats AS (
    SELECT 
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY salary) AS Q1,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY salary) AS Q3
    FROM employees
),
outlier_bounds AS (
    SELECT 
        Q1,
        Q3,
        (Q3 - Q1) AS IQR,
        Q1 - 1.5 * (Q3 - Q1) AS lower_bound,
        Q3 + 1.5 * (Q3 - Q1) AS upper_bound
    FROM salary_stats
)
SELECT 
    e.*,
    ob.lower_bound,
    ob.upper_bound
FROM employees e
CROSS JOIN outlier_bounds ob
WHERE e.salary < ob.lower_bound OR e.salary > ob.upper_bound;

SELECT salary
FROM employees
ORDER BY salary ASC;

WITH salary_stats AS (
    SELECT 
        AVG(salary) AS mean_salary,
        STDDEV(salary) AS stddev_salary
    FROM employees
),
salary_zscore AS (
    SELECT 
        e.*,
        (e.salary - ss.mean_salary) / ss.stddev_salary AS z_score
    FROM employees e
    CROSS JOIN salary_stats ss
)
SELECT *
FROM salary_zscore
WHERE ABS(z_score) > 3;



---------------------------------
-- 6.Standardize and normalize data where applicable to ensure consistency.

CREATE TABLE employees_standardized_normalized AS
WITH salary_stats AS (
    SELECT 
        AVG(salary) AS mean_salary,
        STDDEV(salary) AS stddev_salary
    FROM employees
),
salary_range AS (
    SELECT 
        MIN(salary) AS min_salary,
        MAX(salary) AS max_salary
    FROM employees
),
final_data AS (
    SELECT 
        e.employee_id,
        e.employee_name,
        e.salary,
        e.hireDate,
        e.department,
        (e.salary - ss.mean_salary) / ss.stddev_salary AS standardized_salary,
        (e.salary - sr.min_salary) / (sr.max_salary - sr.min_salary) AS normalized_salary
    FROM employees e
    CROSS JOIN salary_stats ss
    CROSS JOIN salary_range sr
)

SELECT * FROM employees_standardized_normalized


