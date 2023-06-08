-- 코드를 입력하세요
SELECT CAR_ID
from CAR_RENTAL_COMPANY_CAR car
join CAR_RENTAL_COMPANY_RENTAL_HISTORY his using(CAR_ID)
where car_type = "세단" and month(start_date) = 10 
group by car_id
order by car_id desc