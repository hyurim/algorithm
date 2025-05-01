-- https://school.programmers.co.kr/learn/courses/30/lessons/131537
-- 오프라인/온라인 판매 데이터 통합하기 Lv.4

WITH tb1 AS (
    SELECT SALES_DATE,
    PRODUCT_ID,
    USER_ID,
    SALES_AMOUNT
    FROM ONLINE_SALE
    WHERE MONTH(SALES_DATE) = 3

    UNION ALL

    SELECT SALES_DATE,
    PRODUCT_ID,
    NULL as USER_ID,
    SALES_AMOUNT
    FROM OFFLINE_SALE
    WHERE MONTH(SALES_DATE) = 3
    )

SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE,
    PRODUCT_ID,
    USER_ID,
    SALES_AMOUNT
FROM tb1
ORDER BY
1, 2, 3 asc