-- 코드를 입력하세요
SELECT ANIMAL_ID, ins.name
from ANIMAL_INS ins
join ANIMAL_OUTS outs using(animal_id)
order by (outs.datetime - ins.datetime) desc
limit 2