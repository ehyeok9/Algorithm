-- 코드를 입력하세요
SELECT bo.title, re.board_id, re.reply_id, re.writer_id, re.contents, date_format(re.created_date, "%Y-%m-%d")
from used_goods_board bo
join used_goods_reply re using(board_id)
where bo.created_date like "2022-10%"
order by re.created_date, bo.title