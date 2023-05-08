--List Employee details
CREATE VIEW Employee_Sheet AS
SELECT employees.emp_no AS "Employee Number", first_name AS "First Name", last_name AS "Last Name", sex as "Sex", salaries.salary AS "Salary"
FROM employees
INNER JOIN salaries on
salaries.emp_no = employees.emp_no;

SELECT * FROM Employee_Sheet;

--Employee Hired 1986
CREATE VIEW "Employees Hired(1986)" AS
SELECT first_name AS "First Name", last_name AS "Last Name", "hire-date" AS "Hire Date"
FROM employees
WHERE "hire-date" BETWEEN '1986-01-01' AND '1986-12-31';

SELECT * FROM "Employees Hired(1986)";

--Department Manager Details
CREATE VIEW "Department Manager" AS
SELECT departments.dept_no, departments.dept_name, dept_manager.emp_no, employees.first_name, employees.last_name
FROM departments
INNER JOIN dept_manager on 
departments.dept_no = dept_manager.dept_no
INNER JOIN employees on
dept_manager.emp_no = employees.emp_no;

SELECT * FROM "Department Manager";

--Department Employee Details
CREATE VIEW "Department Employees" AS
SELECT dept_emp.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM departments
INNER JOIN dept_emp ON
dept_emp.dept_no = departments.dept_no
INNER JOIN employees ON
dept_emp.emp_no = employees.emp_no;

SELECT * FROM "Department Employees";

--Hercules Employee
CREATE VIEW "Find Hercules" AS
SELECT first_name AS "First Name", last_name AS "Last Name", sex AS "Sex"
FROM employees
WHERE first_name = 'Hercules' 
AND last_name LIKE 'B%';

SELECT * FROM "Find Hercules";

-- Sales Department Employees
CREATE VIEW "Sales Team" AS
SELECT employees.emp_no AS "Employee Number", employees.last_name AS "Last Name", employees.first_name AS "First Name", departments.dept_name AS "Department Name"
FROM employees
INNER JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
INNER JOIN departments ON dept_emp.dept_no = departments.dept_no
WHERE departments.dept_name = 'Sales';

SELECT * FROM "Sales Team";

-- Find all employees in Sales & Development department
CREATE VIEW "Sales/Development employees" AS
SELECT employees.emp_no AS "Employee Number", employees.last_name AS "Last Name", employees.first_name AS "First Name", departments.dept_name AS "Department Name"
FROM employees
INNER JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
INNER JOIN departments ON dept_emp.dept_no = departments.dept_no
WHERE dept_name = 'Sales' 
OR dept_name = 'Development';

SELECT * FROM "Sales/Development employees";

--Employee LastName Frequency
CREATE VIEW "LastName Frequency" AS
SELECT last_name, COUNT(last_name) AS "LastName Frequency"
FROM employees
GROUP BY (last_name) ORDER BY "LastName Frequency" DESC;

SELECT * FROM "LastName Frequency";

SELECT * FROM employees
WHERE sex = 'M'
AND birth_date BETWEEN '1950-01-01' AND '1960-12-31';

SELECT * 
FROM employees
WHERE emp_no IN
(
	SELECT emp_no
	FROM dept_emp
	WHERE dept_no = 'd004'
);

-- Employees making $100000 or more
SELECT salaries.salary, employees.first_name, employees.last_name, employees.sex
FROM salaries
INNER JOIN employees ON 
employees.emp_no = salaries.emp_no
WHERE salary > 100000;
