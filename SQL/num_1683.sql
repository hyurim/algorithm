-- https://leetcode.com/problems/invalid-tweets/description/?envType=problem-list-v2&envId=database
-- MySQL

SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15