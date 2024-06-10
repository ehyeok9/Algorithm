-- 코드를 작성해주세요
select info.ITEM_ID, ITEM_NAME
from ITEM_INFO info
join ITEM_TREE tree on info.ITEM_ID = tree.ITEM_ID
where PARENT_ITEM_ID is null
order by info.ITEM_ID asc