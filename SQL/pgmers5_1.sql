-- https://school.programmers.co.kr/learn/courses/30/lessons/301651
-- 멸종위기의 대장균 찾기

WITH 
RECURSIVE tb1 as (
    -- WITH RECURSIVE 재귀 퀴리 생성
    SELECT ID,
    PARENT_ID,
    1 as ID_LEVEL
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    
    UNION ALL
    
    SELECT e.ID,
    e.PARENT_ID,
    t.ID_LEVEL + 1 as ID_LEVEL
    FROM ECOLI_DATA e
    JOIN tb1 t ON e.PARENT_ID = t.ID
)

SELECT COUNT(ID) as 'COUNT',
ID_LEVEL as GENERATION
FROM tb1 t
WHERE NOT EXISTS (
    SELECT 1
    FROM ECOLI_DATA e
    WHERE e.PARENT_ID = t.ID
)
GROUP BY t.ID_LEVEL