### 创建存储过程
```sql
DELIMITER //
 CREATE PROCEDURE GetAllProducts()
   BEGIN
   SELECT *  FROM products;
   END //
DELIMITER ;
```
### 声明变量
```sql
DECLARE variable_name datatype(size) DEFAULT default_value;
SET xxx = xxx;
```
### MySQL存储过程参数
```sql
MODE param_name param_type(param_size)
```
### MySQL存储函数语法
```sql
CREATE FUNCTION function_name(param1,param2,…)
    RETURNS datatype
   [NOT] DETERMINISTIC
 statements
```