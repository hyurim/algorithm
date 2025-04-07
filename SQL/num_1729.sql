-- https://leetcode.com/problems/find-followers-count/description/?envType=problem-list-v2&envId=database
-- MySQL

SELECT user_id, count(follower_id) as followers_count
FROM Followers
GROUP BY user_id
ORDER BY 1 ASC