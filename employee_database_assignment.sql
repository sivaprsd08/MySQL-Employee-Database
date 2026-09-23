CREATE DATABASE employee;

USE employee;

CREATE TABLE Departments (
    department_id INT,
    department_name VARCHAR(100)
);

CREATE TABLE Location (
    location_id INT,
    location VARCHAR(100)
);

CREATE TABLE Employees (
    employee_id INT,
    employee_name VARCHAR(100),
    gender CHAR(1),
    age INT,
    hire_date DATE,
    designation VARCHAR(100),
    department_id INT,
    location_id INT
);

ALTER TABLE Employees
ADD email VARCHAR(100);

ALTER TABLE Employees
MODIFY designation VARCHAR(100);

ALTER TABLE Employees
DROP COLUMN age;

ALTER TABLE Employees
RENAME COLUMN hire_date TO date_of_joining;

DESC Employees;

RENAME TABLE Departments TO Departments_Info;

RENAME TABLE Location TO Locations;

SHOW TABLES;

TRUNCATE TABLE Employees;

DROP TABLE Employees;

DROP DATABASE employee;

CREATE DATABASE employee;

USE employee;

SELECT DATABASE();

CREATE TABLE Departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE
);

DESC Departments;

CREATE TABLE Location (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(100) NOT NULL UNIQUE
);

DESC Location;

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F')),
    age INT CHECK (age >= 18),
    hire_date DATE DEFAULT (CURRENT_DATE),
    designation VARCHAR(100),
    department_id INT,
    location_id INT,

    FOREIGN KEY (department_id)
        REFERENCES Departments(department_id),

    FOREIGN KEY (location_id)
        REFERENCES Location(location_id)
);

DESC Employees;
