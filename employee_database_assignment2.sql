USE employee;

SELECT DISTINCT salary
FROM Employees;

SELECT *
FROM Employees
WHERE salary > 50000
  AND hire_date < '2016-01-01';

SELECT *
FROM Employees
WHERE designation IS NULL;

SET SQL_SAFE_UPDATES = 0;

UPDATE Employees
SET designation = 'Data Scientist'
WHERE designation IS NULL;

SET SQL_SAFE_UPDATES = 1;

SELECT employee_id, employee_name, designation
FROM Employees
WHERE employee_id = 5004;

SELECT age AS Employee_Age,
       salary AS Employee_Salary
FROM Employees;

SELECT *
FROM Employees
ORDER BY department_id ASC, salary DESC;

SELECT *
FROM Employees
WHERE hire_date >= '2018-01-01'
  AND hire_date < '2019-01-01'
ORDER BY hire_date
LIMIT 5;

SELECT SUM(e.salary) AS total_finance_salary
FROM Employees e
JOIN Departments d
    ON e.department_id = d.department_id
WHERE d.department_name = 'Finance';

SELECT MIN(age) AS minimum_age
FROM Employees;

SELECT l.location,
       MAX(e.salary) AS maximum_salary
FROM Location l
LEFT JOIN Employees e
    ON l.location_id = e.location_id
GROUP BY l.location_id, l.location;

SELECT designation,
       AVG(salary) AS average_salary
FROM Employees
WHERE designation LIKE '%Analyst%'
GROUP BY designation;

SELECT department_id,
       COUNT(*) AS employee_count
FROM Employees
GROUP BY department_id
HAVING COUNT(*) < 3;

-- whose average age is below 30
SELECT location_id,
       AVG(age) AS average_age
FROM Employees
WHERE gender = 'F'
GROUP BY location_id
HAVING AVG(age) < 30;

SELECT e.employee_name,
       e.designation,
       d.department_name
FROM Employees e
INNER JOIN Departments d
    ON e.department_id = d.department_id;

SELECT d.department_name,
       COUNT(e.employee_id) AS employee_count
FROM Departments d
LEFT JOIN Employees e
    ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name;

SELECT l.location,
       e.employee_name
FROM Employees e
RIGHT JOIN Location l
    ON e.location_id = l.location_id;