### MySQL索引
索引其实是一张表，该表保存了主键与索引字段，并指向实体表的记录。优化查询，降低增删改性能。
```sql
CREATE INDEX indexName ON mytable(username(length)); 
```
索引分为单列索引、组合索引；单列索引包含普通索引、唯一索引(null可重复)、主键索引(不可重复且非null)。索引主要使用BTREE和HASH实现。  
```sql
EXPLAIN SELECT XXX FORM XXX ......
SHOW INDEX FROM table_name; \G
```