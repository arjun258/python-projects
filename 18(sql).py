CREATE TABLE Personal (
    Empno        INT         NOT NULL UNIQUE,
    Name         VARCHAR(20) NOT NULL,
    Dobirth      DATE        CHECK (Dobirth > '1960-01-12'),
    Native_place VARCHAR(20) NOT NULL,
    Hobby        VARCHAR(20) NOT NULL
);

CREATE TABLE Job (
    Sno       INT         NOT NULL UNIQUE,
    Area      VARCHAR(20) NOT NULL,
    App_date  DATE,
    Salary    INT         CHECK (Salary BETWEEN 4000 AND 10000),
    Retd_date DATE,
    Dept      VARCHAR(20) NOT NULL
);

Queries
SELECT Personal.Empno, Personal.Name, Job.Salary
FROM Personal
JOIN Job ON Personal.Empno = Job.Sno
WHERE Personal.Hobby = 'Sports';

#2 
SELECT Name
FROM Personal
ORDER BY Dobirth ASC
LIMIT 1;

#3
select Area,count(Sno) from Job group by Area;

#4 
SELECT Native_place, Name, Dobirth
FROM Personal
WHERE Dobirth IN (
    SELECT MAX(Dobirth)
    FROM Personal
    GROUP BY Native_place
);

#5 
SELECT Job.Sno, Personal.Name, Personal.Hobby, Job.Salary
FROM Personal, Job
WHERE Personal.Empno = Job.Sno
ORDER BY Job.Salary DESC;

#6 
SELECT Hobby
FROM Personal
WHERE Name = 'Abhay';

#7
SELECT Job.App_date, Personal.Native_place
FROM Personal, Job
WHERE Personal.Empno = Job.Sno
AND (Personal.Name LIKE 'A%' OR Personal.Name LIKE '%d');

#8 
SELECT SUM(Salary) as Retired_Salary_Expense
FROM Job
WHERE Retd_date > '2006-01-20';

#9
SELECT SUM(Job.Salary * 0.10)
FROM Personal, Job
WHERE Personal.Empno = Job.Sno
AND Personal.Hobby = 'Sports';

#10
select Count(Empno) as Employee_number,Hobby from Personal group by Hobby having count(Empno)>=2;

#11
SELECT COUNT(*)
FROM Job
WHERE YEAR(CURDATE()) - YEAR(App_date) >= 20;

#12
SELECT Personal.Name,Personal.Dobirth FROM Personal,Job WHERE Personal.Empno = Job.Sno and  YEAR(CURDATE()) - YEAR(Job.App_date) > 17;

#13
select Personal.Name,Job.Salary from Personal,Job where Personal.Name = Job.Sno and Job.Salary>(select Max(Salary) from Job where Dept = 'Sales');

#14
UPDATE Job, Personal
SET Salary = Salary + Salary * 0.05
WHERE Job.Sno = Personal.Empno
AND (Personal.Hobby = 'Music' OR YEAR(CURDATE()) - YEAR(Job.App_date) >= 3);

#15 Output of 

#16 
INSERT INTO Personal (Empno, Name, Dobirth, Native_place, Hobby)
VALUES (130, 'NewPerson', '1980-05-10', 'Delhi', 'Music');

#17
ALTER TABLE Job
ADD email VARCHAR(50);

#18
CREATE TABLE NewTable AS
SELECT Empno, Name, Hobby
FROM Personal;
#19
CREATE VIEW LessService AS
SELECT Personal.Empno,
       Personal.Name,
       Personal.Dobirth,
       Personal.Native_place,
       Personal.Hobby,
       Job.Sno,
       Job.Area,
       Job.App_date,
       Job.Salary,
       Job.Retd_date,
       Job.Dept
FROM Personal, Job
WHERE Personal.Empno = Job.Sno
  AND (YEAR(Job.Retd_date) - YEAR(Job.App_date)) < 15;

#20
DELETE Job
FROM Job, Personal
WHERE Personal.Empno = Job.Sno
AND Personal.Hobby != 'Sports';

#21
drop table Personal;