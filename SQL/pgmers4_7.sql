-- https://school.programmers.co.kr/learn/courses/30/lessons/301650
-- 특정 세대의 대장균 찾기

WITH RECURSIVE tb1 as (
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

SELECT ID
FROM tb1
WHERE ID_LEVEL = 3