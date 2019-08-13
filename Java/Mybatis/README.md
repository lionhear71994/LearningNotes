######1、XML对应接口  
```
	<mappers>
		<package name="com.android.xxx" />
	</mappers>
```  
######2、数据库列映射到 Java 对象的驼峰式命名属性  
```
	<settings>  
		<settings name="mapUndersocreToCamelCase" value="true" />
	</settings>
```  
######3、多表查询多个返回值类型  
```  
public class SysRole { 
／／其他原有字段． ．．
/** 
用户信息
*/ 
private SysUser user;
```  
/

  
  