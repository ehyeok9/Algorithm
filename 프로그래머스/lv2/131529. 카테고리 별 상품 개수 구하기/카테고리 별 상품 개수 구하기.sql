-- 코드를 입력하세요
with te as(
    select *, substring(product_code, 1, 2) as category
    from product
)
SELECT category, count(*) as PRODUCTS
from te
group by category