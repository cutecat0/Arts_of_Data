#!/usr/bin/env python3
# hive.py

import re
import sys

for line in sys.stdin:
    year, temp, q = line.strip().split()
    if temp != '9999' and re.match('[01459]', q):
        print('%s\t%s' % year, temp)


hive> ADD FILE /users/Gwendolynhai/Hadoop/hive.py;
hive>from records2
    >select transform(year, temperature, quality)
    >using 'hive.py'
    >as year, temperature;


from (
      from records2
      MAP year, temperature, quality
      USING 'is_good_quality.py'
      AS year, temperature
    ) map_output
      REDUCE year, temperature
      USING 'max_temperature_reduce.py'
      AS year, temperature;


# inner join
select table_A.*, table_B.*
from table_A JOIN table_B on (table_A.id = table_B.id);

# use where
select table_A.*, table_B.*
from table_A, table_B
where table_A.id = table_B.id;

explan
select sales.*, things.*
from sales join things on (sales.id = things.id);

# left outer join
# 左边列都在，右边不匹配的直接为null
select sales.*, things.*
from sales left outer join things on (sales.id = things.id);

# right outer join
# 右边列都匹配，左边不匹配的直接为null
select sales.*, things.*
from sales right outer join things on (sales.id = things.id);

# full outer join
# 左右两边所有的都保留
select sales.*, things.*
from sales full outer join things on (sales.id = things.id);

# left semi join
# 半连接
select *
from things
where things.id in (select id from sales);

#above equels to below
select * from things left semi join sales on (sales.id = things.id)

# use left semi join ... on 's limit:
# 右表只能在on子句出现（不能在select表达式中引用右表）



# an idea of video
A professional team only amis at 'How to Improve the Quality of Video', as for content, leave it to someone who only product video
"IP Team" & "Technology Team"


-- map join

SET hive.optimize.bucketmapjoin=true;

# study time 2021-12-27
#hive 对自查询的支持有限
select station, year, AVG(max_temperature)
from (
      select station, year, MAX(temperature) as max_temperature
      from records2
      where temperature != 9999 and quality in (0, 1, 4, 5, 9)
      group by station, year
) mt
group by station, year;


# view 视图
create view valid_records
as
select *
from records2
where temperature != 9999 and quality in (0, 1, 4, 5, 9);


describe extended view_name;

create view max_temperatures (station, year, max_temperature)
as
select station, year, max(temperature) from valid_records
group by station, year;


UDF (user-defined function) 用户定义函数































