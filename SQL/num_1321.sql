-- https://leetcode.com/problems/restaurant-growth/description/
-- 1321. Restaurant Growth
-- Medium

WITH tb1 AS (
    SELECT 
    visited_on,
    SUM(amount) OVER (
        ORDER BY visited_on
        RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW 
    ) AS amount
    FROM Customer
)

SELECT 
    visited_on,
    amount,
    ROUND(amount/7,2) as average_amount
FROM tb1
WHERE DATEDIFF(visited_on, (SELECT MIN(visited_on) FROM Customer)) >= 6
GROUP BY visited_on