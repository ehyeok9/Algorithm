select DATE_FORMAT(SALES_DATE, "%Y-%m-%d"), PRODUCT_ID, USER_ID, SALES_AMOUNT
from 
(
    SELECT SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
    from ONLINE_SALE
    where SALES_DATE like "2022-03%"
    
    union all
    
    select SALES_DATE, PRODUCT_ID, null as USER_ID, SALES_AMOUNT
    from OFFLINE_SALE
    where SALES_DATE like "2022-03%"

) as sales_data
order by SALES_DATE, PRODUCT_ID, USER_ID ;