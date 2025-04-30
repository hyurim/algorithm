-- https://leetcode.com/problems/sales-person/
-- Easy

SELECT p.name
FROM SalesPerson p
WHERE p.sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders o 
    LEFT JOIN Company c ON c.com_id = o.com_id
    WHERE c.name = "RED"
)
