SELECT Employee.EMPLOYEEID, Employee.NAME, Employee.JOBID, Job.JOBTITLE FROM Employee JOIN Job ON Employee.JOBID = Job.JOBID;
#2
SELECT Employee.NAME, Employee.SALES, Job.JOBTITLE
FROM Employee
JOIN Job ON Employee.JOBID = Job.JOBID
WHERE Employee.SALES > 1300000;

#3
SELECT Employee.NAME, Job.JOBTITLE
FROM Employee
JOIN Job ON Employee.JOBID = Job.JOBID
WHERE Employee.NAME LIKE '%SINGH%';
#4
The foreign key in EMPLOYEE is: JOBID
#5
UPDATE Employee
SET JOBID = 104
WHERE EMPLOYEEID = 'E4';



