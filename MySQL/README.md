### UUID
* 可通过SELECT UUID()生成
* 在MySQL中，可以以紧凑格式(BINARY)存储UUID值
* INSERT INTO table VALUES(UUID(),...);
### 查找重复值 
```sql
GROPU BY XXX HAVING COUNT(XXX) > 1  
```
### 删除重复行
```sql
INNER JION WHERE t1.id < t1.id AND t1.xxx = t2.xxx
```
### 获取MySQL两个或多个表的行计数
UNION  
### 使用一个查询获取数据库中所有表的MySQL行计数  
```sql
SELECT table_name, table_rows FROM information_schema.tables
WHERE table_schema = 'XXX' ORDER BY table_rows desc;
```
如不准确，查询前运行ANALYZE TABLE table_name语句。  
### 比较两个表
```sql
SELECT pk, c1 FROM
 ( SELECT t1.pk, t1.c1 FROM t1 UNION ALL SELECT t2.pk, t2.c1 FROM t2)  t
GROUP BY pk, c1 HAVING COUNT(*) = 1 ORDER BY pk
```
### 将表复制到新表
```sql
CREATE TABLE new_table (子查询)
```
### 比较相同表中的连续行
```sql
table_1 INNER JOIN table_2 ON table_1.id = table_2.id + 1
```
ON条件用于当前行与下一行比较(id连续性，不连续可创建新连续列实现)
###正则表达式(REGEXP运算符) 
```sql
WHERE column REGEXP pattern;
```
### 选择第n个最高纪录
```sql
ORDER BY column ASC/DESC LIMIT n-1,n;
```
### 重置自动增量值
```sql
ALTER TABLE table_name AUTO_INCREMENT = value;
```
### 获取今天
```sql
CURDATE();
DATE(NOW());
```
### SQL获取id为奇数值
WHERE mod(id,2) = 1;
### 交换值
```sql
UPDATE salary SET sex = if(sex = 'f', 'm', 'f');
```

