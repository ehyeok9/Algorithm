-- 코드를 입력하세요
SELECT USER_Id, nickname, concat(city, " ", STREET_ADDRESS1, " ", STREET_ADDRESS2) as "전체주소",
     concat(substring(TLNO, 1, 3),"-",substring(TLNO, 4, 4),"-",substring(TLNO, 8, 4)) as "전화번호"
from USED_GOODS_BOARD bo
join USED_GOODS_USER us on bo.WRITER_ID = us.user_id
group by writer_id
having count(*) >= 3
order by user_id desc