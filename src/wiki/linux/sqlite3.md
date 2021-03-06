---
layout: page
date: 20220412000000
title: sqlite3
categories:
tags: [sql]
udc: 
---

## sqlite3

### cli

```bash
sqlite3 'from_this_db.db' '.dump' | sqlite3 -batch 'to_this_db.db'
    # 合并db


sqlite3 'a.db' '.dump' | sqlite3 -batch 'aa.db'
    # 合并db


sqlite3 in.db .dump > in.sql
    # .db to .sql


sqlite3 in.db < in.sql
    # .sql to .db


sqlite3 -csv anime.db ".import anime.csv table1"
    # .csv to .db


sqlite3 -separator ',' anime.db '.import new.csv "1917-2018"'
    # .csv to .db
    # 把 anime.csv 导入到 anime.db 中的表 1917-2018


sqlite3 en.db 'VACUUM;'
    # 压缩db
    # 压缩 en.db 的体积


sqlite3 -header -csv Animes.db 'select * from "1917-2018";' > animes.csv
    # .db to .csv
    # 表名放在双引号内


sqlite3 in.db < in.sql
    # 运行 .sql


cat in.csv | sqlite3 in.db
    # 运行 .sql


```

### sqlite

```sqlite
.database
    # 查看加载了的数据库


.schema
    # 查看现有的表的信息


.tables
    # 查看现有的表



```


### sql

```sql
# 设置默认值
CREATE TABLE _tab (
    __col TEXT DEFAULT "default value",
);


# 避免重复添加列
CREATE TABLE _tab (
    __id INTEGER,
    __gid INTEGER,
    UNIQUE(__id, __gid) -- 为 __id和__gid 启用去重 
); 
insert or replace into _tab(__id,__gid) values (1,0); 
    -- 如果不存在 则添加
    -- 如果存在 则更新
insert or ignore into _tab (__id,__gid) values (2,0);
    -- 如果存在 则忽略
    -- 如果不存在 则添加


-- 避免重复添加表
create table if not exists _tab ( -- 选择性添加表
    __id integer,
    __gid integer
); 


-- regex
select * from field
where context REGEXP '^${context},|,${context},|^${context}$|,${context}$'


-- 最后一行求总和
SELECT
    IFNULL(u.status, '合计') 状态, COUNT(*)
FROM
    user u
GROUP BY u.status WITH ROLLUP

```

```sql
SELECT * FROM _tab;
    # 从表 _tab 中获取 全部的数据


SELECT __col1,__col2 FROM _tab;
    # 从表 _tab 中获取 __col1和__col2 的数据


select 10+2;
    # 计算 10+2


SELECT * FROM _tab WHERE A > 500 OR B != 700;
    # 从表 _tab 中获取 * (全部的)记录/内容
    # 然后 筛选出 A 字段下的 值大于500 的内容
    # 或者 筛选出 B 字段下的 值不是700 的内容(仅当 A > 500 不成立时才会执行这句)


SELECT * FROM _tab WHERE A IS NOT NULL;
    # 从表 _tab 中获取 * (全部的)记录/内容
    # 然后 筛选出 A 字段下的 值不是NULL (不为空)的内容


SELECT * FROM _tab WHERE A GLOB 'R*';
    # 从表 _tab 中获取 * (全部的)记录/内容
    # 然后 筛选出 A 字段下的 以R开头 的内容


SELECT * FROM _tab WHERE A (25, 27);
    # 从表 _tab 中获取 * (全部的)记录/内容
    # 然后 筛选出 A 字段下的 值为25或27 的内容


SELECT DISTINCT __col FROM _tab;
    # 查询以 _tab 中的 __col 为标准去重的结果



select * from _tab order by __col 
    # 排序


SELECT name FROM SQLITE_MASTER WHERE type='table' ORDER BY name;
    # 列出已有的表


DROP TABLE _tab;
    # 删除表 _tab


INSERT INTO _tab VALUES (7, 'James', 24, 'Houston', 10000.00 );
    # 为表 _tab 创建记录


UPDATE anime SET 'year'='TV' WHERE year GLOB 'T*';
    # 从表 anime 中将 year字段下的所以内容改为TV
    # 但只对 year字段下以T开头值生效(这里用 WHERE 做了限制  以防止误操作)


alter table _tab add __col char;
    # 增加列


alter table _tab alter column __col varchar(4000);
    # 修改列类型


alter table _tab drop column __col;
    # 删除列


ALTER TABLE Anime RENAME TO ID;
    # 修改表名
    # 将表名 Anime 修改为 ID


ALTER TABLE Anime RENAME COLUMN two TO new;
    # 修改列名
    # 将表 Anime 中的列名 two 修改为 new


ATTACH DATABASE 'in.db' as 'IN';
    # 将 in.db 附加到 IN (可理解为创建副本)


attach database 'in.db' as 'IN';
    # 上下等价(sql 不区分大小写)


DETACH DATABASE 'IN';
    # 从数 .db 中分离 IN


delete from _tab where _tab.rowid not in (select MAX(_tab.rowid) from _tab group by __col);
    # 以 __col 为标准删除 _tab 里的重复数据



```


### learn

[Quick Reference](https://www.w3schools.com/sql/sql_quickref.asp)

#### 转义

```sql
-- 转义 ' 单引号
-- your''s 等于 your's
INSERT INTO _tab VALUES('your''s');



```

####

用insert语句插入数据, 为避免重复插入又不打断数据处理。
首先要避免重复插入, 就必须在插入时引发冲突。
在表中设置了id字段, 该字段为UNIQUE属性, 当插入的id已存在时引发冲突。
引发冲突后insert会做一些处理, 处理方式由OR字句定义。包含如下：

+ ROLLBACK  
当发生约束冲突, 立即ROLLBACK, 即结束当前事务处理, 命令中止并返回SQLITE_CONSTRAINT代码。
若当前无活动事务(除了每一条命令创建的默认事务以外), 则该算法与ABORT相同。
+ ABORT  当发生约束冲突, 命令收回已经引起的改变并中止返回SQLITE_CONSTRAINT。
但由于不执行ROLLBACK, 所以前面的命令产生的改变将予以保留。
缺省采用这一行为。
+ FAIL  当发生约束冲突, 命令中止返回SQLITE_CONSTRAINT。
但遇到冲突之前的所有改变将被保留。
例如, 若一条UPDATE语句在100行遇到冲突100th, 前99行的改变将被保留, 而对100行或以后的改变将不会发生。
+ IGNORE  当发生约束冲突, 发生冲突的行将不会被插入或改变。
但命令将照常执行。在冲突行之前或之后的行将被正常的插入和改变, 且不返回错误信息。
+ REPLACE  当发生UNIQUE约束冲突, 先存在的, 导致冲突的行在更改或插入发生冲突的行之前被删除。
这样, 更改和插入总是被执行。命令照常执行且不返回错误信息。当发生NOT NULL约束冲突, 导致冲突的NULL值会被字段缺省值取代。若字段无缺省值, 执行ABORT算法
  
为避免操作打断, 我选择了IGNORE。最后完整的用法如下：
INSERT OR IGNORE INTO troopstypes (id)values(2);
   

#### 数据类型

+ NULL  
    + 空值
+ INTEGER  
    + 8-byte 长度的整数
+ REAL  
    +  8-byte 长度的浮点数
+ NUMERIC
+ TEXT   
    + 字符串
+ BLOB   
    + 二进制数据
+ json1
    + json 格式的数据

+ bool
    + 布尔值需使用 INTEGER 代替
1 为 true
0 为 false
+ time
    + 日期值
    + TEXT 识别 YYYY-MM-DD HH:MM:SS.SSS
    + INTEGER
    + REAL



#### 主键与唯一索引

主键[primary key]
唯一索引[unique index]

+ 主键
    + 主键约束比唯一索引约束严格
    + 没有主键时  非空唯一索引自动成为主键
    + 主键不允许空值
    + 一个表中主键只能有一个
    + 主键产生唯一的聚集索引


+ 唯一性索引
    + 一个表中可以有多个唯一性索引
    + 唯一性索引列允许空值
    + 索引可以提高查询的速度
    + 唯一索引产生唯一的非聚集索引


(聚集索引确定表中数据的物理顺序)



数据库连接池大小的设置
连接数 = ((核心数 * 2) + 有效磁盘数)

