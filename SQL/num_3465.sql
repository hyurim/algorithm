-- https://leetcode.com/problems/find-products-with-valid-serial-numbers/description/?envType=problem-list-v2&envId=database
-- MySQL


SELECT * 
FROM products
WHERE description LIKE '%SN____-____'
OR description LIKE '%SN____-____ %'