-- https://school.programmers.co.kr/learn/courses/30/lessons/133027
-- 주문량이 많은 아이스크림들 조회하기

SELECT j.FLAVOR
FROM (SELECT FLAVOR,
      SUM(TOTAL_ORDER) AS total
      FROM JULY 
      GROUP BY FLAVOR
      ) AS j
JOIN FIRST_HALF f ON f.FLAVOR = j.FLAVOR
ORDER BY (j.total + f.TOTAL_ORDER) DESC
LIMIT 3