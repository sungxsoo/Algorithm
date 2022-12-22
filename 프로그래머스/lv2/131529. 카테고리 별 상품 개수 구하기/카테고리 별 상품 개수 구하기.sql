-- 코드를 입력하세요

SELECT
        LEFT(PRODUCT_CODE, 2) as PRODUCT_CODE_SHORT,
        count(*)
FROM
        PRODUCT
GROUP BY
        PRODUCT_CODE_SHORT