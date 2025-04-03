-- https://leetcode.com/problems/find-valid-emails/description/?envType=problem-list-v2&envId=database
-- MySQL

SELECT *
FROM Users
WHERE email REGEXP '^[A-Za-z0-9]+@[A-Za-z]+\\.com'