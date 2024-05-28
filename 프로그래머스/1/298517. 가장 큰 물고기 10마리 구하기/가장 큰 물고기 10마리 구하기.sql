select ID, LENGTH
from (
    select *
    from FISH_INFO
    order by length desc, id asc
) a
limit 10