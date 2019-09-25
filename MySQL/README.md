### UUID
* 可通过SELECT UUID()生成
* 在MySQL中，可以以紧凑格式(BINARY)存储UUID值
* INSERT INTO table VALUES(UUID(),...);
##### 查找重复值 
```sql
GROPU BY XXX HAVING COUNT(XXX) > 1  
```
##### 删除重复行
```sql
INNER JION WHERE t1.id < t1.id AND t1.xxx = t2.xxx
```
##### 获取MySQL两个或多个表的行计数
UNION  
##### 使用一个查询获取数据库中所有表的MySQL行计数  
```sql
SELECT table_name, table_rows FROM information_schema.tables
WHERE table_schema = 'XXX' ORDER BY table_rows desc;
```
如不准确，查询前运行ANALYZE TABLE table_name语句。  
##### 比较两个表
```sql
SELECT pk, c1 FROM
 ( SELECT t1.pk, t1.c1 FROM t1 UNION ALL SELECT t2.pk, t2.c1 FROM t2)  t
GROUP BY pk, c1 HAVING COUNT(*) = 1 ORDER BY pk
```
##### 将表复制到新表
```sql
CREATE TABLE new_table (子查询)
```


