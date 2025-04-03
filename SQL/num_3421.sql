-- https://leetcode.com/problems/find-students-who-improved/description/?envType=problem-list-v2&envId=database
-- MySQL

with tb1 as (
    SELECT student_id,
    subject,
    FIRST_VALUE(score) OVER (PARTITION BY student_id,subject ORDER BY exam_date) AS first_score,
    FIRST_VALUE(score) OVER (PARTITION BY student_id,subject ORDER BY exam_date DESC) AS latest_score
FROM Scores
)

SELECT DISTINCT *
FROM tb1
WHERE latest_score > first_score