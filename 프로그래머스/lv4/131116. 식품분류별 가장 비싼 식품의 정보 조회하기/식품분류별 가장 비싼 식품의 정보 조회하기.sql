-- 코드를 입력하세요
# SELECT CATEGORY, PRICE
# FROM FOOD_PRODUCT
# WHERE CATEGORY = '과자' OR CATEGORY = '국' OR CATEGORY = '식용유' OR CATEGORY = '김치' 
# GROUP BY CATEGORY
# ORDER BY PRICE DESC

SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT as F WHERE F.CATEGORY = FOOD_PRODUCT.CATEGORY)
GROUP BY CATEGORY
HAVING CATEGORY = '과자' OR CATEGORY = '국' OR CATEGORY = '식용유' OR CATEGORY = '김치' 
ORDER BY MAX_PRICE DESC
