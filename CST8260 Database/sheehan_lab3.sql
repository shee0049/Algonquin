
DROP DATABASE IF EXISTS ACME;
CREATE DATABASE ACME;
USE ACME;

DROP TABLE IF EXISTS employee;
CREATE TABLE employee (
	EmplID INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
	EmplFname varchar(25) NOT NULL,
	EmplLname varchar(25) NOT NULL,
	EmplOffice varchar(5) NOT NULL,
    EmplPhone varchar(25),
	EmplDept INT,
    foreign key(EmplDept) references department(DeptID)
)CHARSET utf8;

DROP TABLE IF EXISTS department;
CREATE TABLE department (
	DeptID INT PRIMARY KEY UNIQUE,
	DeptName VARCHAR(25) NOT NULL,
	DeptOffice VARCHAR(5) NOT NULL,
	DeptPhone VARCHAR(25),
	DeptSupervisor INT,
    foreign key(DeptSupervisor) references employee(EmplID)
)DEFAULT CHARSET utf8;

DROP TABLE IF EXISTS project; 
CREATE TABLE project(
	ProjectId INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
	ProjectClient VARCHAR(15) NOT NULL,
    ProjectLead INT,
	ProjectContactPhone VARCHAR (25),
    foreign key(ProjectLead) references employee(EmplId)
)DEFAULT CHARSET utf8;

# Value inserts for the employee table
INSERT INTO employee(EmplFname, EmplLname, EmplOffice, EmplPhone, EmplDept)
VALUES ("John", "Doe", "B101","613-556-7098", 1);
INSERT INTO employee(EmplFname, EmplLname, EmplOffice, EmplPhone, EmplDept)
VALUES ("Jane", "Robinson", "B102","613-427-7510", 1);
INSERT INTO employee(EmplFname, EmplLname, EmplOffice, EmplPhone, EmplDept)
VALUES ("Mario", "Lemieux", "B103", "613-412-1421", 2);
INSERT INTO employee(EmplFname, EmplLname, EmplOffice, EmplPhone, EmplDept)
VALUES ("Gordie", "Howe", "B104", "613-472-2131", 3);
INSERT INTO employee(EmplFname, EmplLname, EmplOffice, EmplPhone, EmplDept)
VALUES ("Mr.", "Supervisior", "C105", "613-149-3841", 1);
INSERT INTO employee(EmplFname, EmplLname, EmplOffice, EmplPhone, EmplDept)
VALUES ("Adam", "Jensen", "C124", "613-831-9234", 4);

#Value inserts for the department table 
INSERT INTO department(DeptId, DeptName, DeptOffice, DeptPhone, DeptSupervisor)
VALUES(1, "Sales", "C106", "612-646-8137", 5);
INSERT INTO department(DeptId, DeptName, DeptOffice, DeptPhone, DeptSupervisor)
VALUES(2, "Development", "B110", "612-214-4124", 1);
INSERT INTO department(DeptId, DeptName, DeptOffice, DeptPhone, DeptSupervisor)
VALUES(3, "Accounting", "A120", "612-317-6431", 2);
INSERT INTO department(DeptId, DeptName, DeptOffice, DeptPhone, DeptSupervisor)
VALUES(4, "Security", "CD500", "614-476-9183", 6);

#Value inserts for project table
INSERT INTO project(ProjectClient, ProjectLead, ProjectContactPhone)
VALUES("Sarif In.", 6, "613-427-7510");
INSERT INTO project(ProjectClient, ProjectLead, ProjectContactPhone)
VALUES("Tai-Young Med", 3, "613-412-1421");
INSERT INTO project(ProjectClient, ProjectLead, ProjectContactPhone)
VALUES("Umbrella Corp.", 4, "613-472-2131");