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

