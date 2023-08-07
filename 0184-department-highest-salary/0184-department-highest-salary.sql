# Write your MySQL query statement below
SELECT Department, Employee, Salary
FROM (
    SELECT
        d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        DENSE_RANK() OVER (PARTITION BY d.id ORDER BY e.salary DESC) as SalaryRank
    FROM Department d
    INNER JOIN Employee e
    ON d.id = e.departmentId
) AS temp
WHERE SalaryRank = 1;

