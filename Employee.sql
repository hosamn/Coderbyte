-- SQL Employee Salaries

-- In this MySQL challenge, your query should return the information for the employee
-- with the third highest salary. Write a query that will find this employee and return
-- that row, but then replace the DivisionID column with the corresponding DivisionName
-- from the table cb_companydivisions.
-- You should also replace the ManagerID column with the ManagerName if the ID exists
-- in the table and is not NULL.

-- Your output should look like the following table.
-- https://coderbytestaticimages.s3.amazonaws.com/editor/challenges/ascii_salaries.png


/* write your SQL query below */

SELECT 
    t1.ID,
    t1.Name,
    t2.DivisionName,
    t3.Name as ManagerName, 
    t1.Salary
FROM
  (SELECT *
   FROM maintable_KFTZ2
   ORDER BY Salary DESC
   LIMIT 3)
as t1
INNER JOIN cb_companydivisions as t2
ON t1.DivisionID = t2.ID
INNER JOIN maintable_KFTZ2 as t3
ON t1.ManagerID = t3.ID
ORDER BY Salary
LIMIT 1