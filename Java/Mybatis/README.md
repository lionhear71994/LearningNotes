1、XML对应接口  
```
	<mappers>
		<package name="com.android.xxx" />
	</mappers>
```  
2、数据库列映射到 Java 对象的驼峰式命名属性  
```
	<settings>  
		<settings name="mapUndersocreToCamelCase" value="true" />
	</settings>
```  
3、多表查询多个返回值类型  
```  
public class SysRole { 
／／其他原有字段． ．．
/** 
用户信息
*/ 
private SysUser user;
```  
4、数据库类型的datetime类型存储DATE和TIMESTAMP两种类型。  
  
5、获取主键的值  
	a.useGeneratedKeys 设置为true后，MyBatis会使用JDBCgetGeneratedKeys方法来取出 由数据库内部生成的主键。获得主键值后将其赋值给 keyProperty 配置的 id 属性。  
	b.代码如下：```  
	<selectKey keyColumn=” id” resultType=” long” keyProperty=” id” order=” AFTER” >
		SELECT LAST INSERT ID () 
	</selectKey>
	```  
6、多参数查询使用@Param  
  
7、Mybatis 也可以通过注解写SQL语句，比如@Select,@Insert...  不推荐该种方式
 ```@Select ({ ” select id, role name roleName, enabled, 
		create_by createBy, 
		create time createTime ” 
		” from sys_role ”, 
		” where id= #{id } ” }) 
	SysRole selectByid(Long id) ;
```	  

8、动态SQL OGNL  
 ```<if test="true/false">
		user_name={userName},
	</if>```  
	if语句需考虑全为null时SQL语法是否错误问题  
	choose用法
 ```<choose>
		<when test="true/false"> ... </when>
		<otherwise>...</otherwise>
	</choose>```  
	where用法：如果该标签包含的元素中有返回值，就插入where ；如果where后面字符以AND、OR开头的，就将它们剔除。  
 ```<trim prefix="SET" 	suffixOverrides=",">...</trim>```
 ```<foreach collectin="list" open="(" close=” )” separator=” , ” item=” id” index=” i ” >
		#{id} 
	</foreach>```  
	collectin属性可在接口使用@Param指定名字。  
	<bind narne= userNarneLike value="’%’＋ userNarne +'%'” />	----拼接字符串  
	
9、代码生成器 
  
  