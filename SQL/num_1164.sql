-- https://leetcode.com/problems/product-price-at-a-given-date/
-- Medium

WITH cte AS (
    SELECT 
        product_id,
        CASE WHEN change_date > '2019-08-16' THEN 10 ELSE new_price END AS price,
        change_date
    FROM Products
),
ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY 
               CASE WHEN change_date <= '2019-08-16' THEN change_date ELSE NULL END DESC,
               change_date ASC 
           ) AS rn
    FROM cte
)

SELECT product_id, price
FROM ranked
WHERE rn = 1;