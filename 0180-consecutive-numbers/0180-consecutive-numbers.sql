# Write your MySQL query statement below
SELECT DISTINCT a.num AS ConsecutiveNums
FROM Logs a
INNER JOIN Logs b ON b.id = a.id + 1 AND b.num = a.num
INNER JOIN Logs c ON c.id = a.id + 2 AND c.num = a.num;