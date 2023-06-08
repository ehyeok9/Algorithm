-- 코드를 입력하세요
with te as (
    select FOOD_TYPE, max(favorites) as max_val
    from REST_INFO
    group by food_type
)

select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from REST_INFO re
join te using(food_type)
where favorites = max_val
order by food_type desc