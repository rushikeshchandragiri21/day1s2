CREATE DATABASE assign4;

USE assign4;
SELECT name FROM sys.databases;


SELECT * FROM information_schema.tables WHERE table_type = 'BASE TABLE';


CREATE DATABASE assign4;

USE assign4;

SELECT * FROM information_schema.tables WHERE table_type = 'BASE TABLE';

-- Create the Employees table
CREATE TABLE Employees (
  id INT PRIMARY KEY IDENTITY(1,1),
  name VARCHAR(50) NOT NULL,
  gender CHAR(1) NOT NULL,
  salary DECIMAL(10,2) NOT NULL,
  department VARCHAR(20) NOT NULL
);

-- View the structure of the Employees table
EXEC sp_columns 'Employees';

-- Insert data into the Employees table
INSERT INTO Employees (name, gender, salary, department) VALUES
('John Doe', 'M', 85000.00, 'Sales'),
('Jane Smith', 'F', 72000.50, 'Marketing'),
('Alice Jones', 'F', 68500.75, 'Engineering'),
('David Lee', 'M', 90000.00, 'Management'),
('Michael Brown', 'M', 75000.00, 'Sales'),
('Emily Davis', 'F', 68000.25, 'Marketing'),
('Robert Johnson', 'M', 80000.00, 'Engineering'),
('Sarah Wilson', 'F', 71000.75, 'Management'),
('Daniel Martinez', 'M', 82000.00, 'Sales'),
('Olivia Thomas', 'F', 70000.50, 'Marketing'),
('Matthew White', 'M', 77000.25, 'Engineering'),
('Sophia Anderson', 'F', 69000.75, 'Management'),
('William Harris', 'M', 84000.00, 'Sales'),
('Isabella Lewis', 'F', 73000.50, 'Marketing'),
('James Robinson', 'M', 78000.25, 'Engineering'),
('Amelia Garcia', 'F', 72000.75, 'Management'),
('Ethan Jackson', 'M', 86000.00, 'Sales'),
('Ava Martinez', 'F', 74000.50, 'Marketing'),
('Benjamin Thompson', 'M', 79000.25, 'Engineering'),
('Mia Davis', 'F', 73000.75, 'Management'),
('Alexander Wilson', 'M', 88000.00, 'Sales'),
('Charlotte Thomas', 'F', 75000.50, 'Marketing'),
('Jacob Brown', 'M', 80000.25, 'Engineering'),
('Harper Johnson', 'F', 74000.75, 'Management'),
('Liam Martinez', 'M', 90000.00, 'Sales'),
('Grace Anderson', 'F', 76000.50, 'Marketing'),
('Daniel Harris', 'M', 81000.25, 'Engineering'),
('Ella Thompson', 'F', 75000.75, 'Management'),
('Logan Garcia', 'M', 87000.00, 'Sales'),
('Avery Wilson', 'F', 77000.50, 'Marketing'),
('Jackson Thomas', 'M', 82000.25, 'Engineering'),
('Sofia Lee', 'F', 76000.75, 'Management'),
('Mason Martinez', 'M', 89000.00, 'Sales'),
('Chloe Brown', 'F', 78000.50, 'Marketing'),
('Lucas Johnson', 'M', 83000.25, 'Engineering'),
('Zoe Wilson', 'F', 78000.75, 'Management'),
('Liam Harris', 'M', 91000.00, 'Sales'),
('Emma Thompson', 'F', 79000.50, 'Marketing'),
('Noah Garcia', 'M', 84000.25, 'Engineering'),
('Aria Davis', 'F', 79000.75, 'Management'),
('James Wilson', 'M', 92000.00, 'Sales'),
('Ava Johnson', 'F', 80000.50, 'Marketing'),
('Oliver Martinez', 'M', 85000.25, 'Engineering'),
('Ella Brown', 'F', 80000.75, 'Management'),
('William Lee', 'M', 93000.00, 'Sales'),
('Isabella Thompson', 'F', 81000.50, 'Marketing');

-- Select all records from the Employees table
SELECT * FROM Employees;


SELECT department, SUM(salary) as Total FROM Employees GROUP BY department;



SELECT department, SUM(salary) as Total FROM Employees GROUP BY department WITH ROLLUP;

SELECT coalesce(department,'Total Sum'), SUM(salary) as Total FROM Employees GROUP BY department WITH ROLLUP; -- coalesce is use to replace null value in that column with the second argument


SELECT coalesce(department,'Total Sum'),coalesce(gender,'Sum'), SUM(salary) as Total FROM Employees GROUP BY department,gender WITH ROLLUP;



-- CUBE Operator : --->

SELECT department, gender, SUM(salary) AS Total
FROM Employees
GROUP BY CUBE(department, gender);




SELECT COALESCE(department,'SUM') as Department, COALESCE(gender,'SUM') as Gender, SUM(salary) AS Total
FROM Employees
GROUP BY CUBE(department, gender);

SELECT SYSDATE();

SELECT COALESCE(department,'SUM') as Department, COALESCE(gender,'SUM') as Gender, SUM(salary) AS Total
FROM Employees
GROUP BY GROUPING SETS ((department, gender), (department), (gender), ());




SELECT department, gender, SUM(salary) AS Total
FROM Employees
WHERE department = 'Engineering' -- Specify the department you want to drill down into
GROUP BY GROUPING SETS ((department, gender), ());