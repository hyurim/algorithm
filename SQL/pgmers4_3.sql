-- https://school.programmers.co.kr/learn/courses/30/lessons/59413
-- 입양 시각 구하기(2)

WITH RECURSIVE hours AS (
  SELECT 0 AS 'HOUR'
  UNION ALL
  SELECT hour + 1 FROM hours
  WHERE hour < 23
)

SELECT h.HOUR,
COUNT(a.DATETIME)
FROM ANIMAL_OUTS a
RIGHT JOIN hours h ON h.HOUR = HOUR(a.DATETIME)
GROUP BY 1
ORDER BY 1 ASC

-- RECURSIVE 재귀