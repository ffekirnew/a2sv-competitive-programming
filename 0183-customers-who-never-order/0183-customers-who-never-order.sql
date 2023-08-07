# Write your MySQL query statement below
SELECT Customers
FROM (
    SELECT c.id AS customerId, c.name as Customers, o.id AS orderId, o.customerId as orderCustomerId
    FROM Customers c
    LEFT JOIN Orders o ON c.id = o.customerId
) AS temp
WHERE orderId IS NULL;