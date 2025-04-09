-- https://school.programmers.co.kr/learn/courses/30/lessons/284528
-- LEVEL 4
with GRADE as (
    SELECT EMP_NO,
    CASE 
        WHEN AVG(SCORE) >= 96 THEN 'S'
        WHEN AVG(SCORE) >= 90 THEN 'A'
        WHEN AVG(SCORE) >= 80 THEN 'B'
        ELSE 'C'
    END as 'grade'
    FROM HR_GRADE
    GROUP BY EMP_NO
)

SELECT e.EMP_NO as 'EMP_NO',
e.EMP_NAME as 'EMP_NAME',
g.grade as 'GRADE',
CASE
    WHEN g.grade = 'S' THEN e.SAL*0.20
    WHEN g.grade = 'A' THEN e.SAL*0.15
    WHEN g.grade = 'B' THEN e.SAL*0.10
    ELSE 0
END as 'BONUS'
FROM HR_EMPLOYEES e
JOIN GRADE g ON g.EMP_NO = e.EMP_NO
