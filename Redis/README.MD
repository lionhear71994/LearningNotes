SET GET INCR DEL  
删除前保留时间： 	EXPIRE   
查看删除时间(配合上面命令使用):	TTL  
  
A list is a series of ordered values.  
	RPUSH, LPUSH, LLEN(长度), LPOP, RPOP,LRANGE(分片)  
A set is similar to a list, except it does not have a specific order and each element may only appear once.	  
	SADD, SREM, SISMEMBER(查询), SMEMBERS(returns a list of all the members of this set.) and SUNION(combines two or more sets and returns the list of all elements.).  
  
Sorted Set:	ZADD xxx 1 "xxx"	ZRANGE 2 4  
  
Hashes:	HSET HGET HGETALL HMSET(at once) 
	HSET user:1000 visits 10  
    HINCRBY user:1000 visits 1 => 11  
    HINCRBY user:1000 visits 10 => 21  
    HDEL user:1000 visits  
    HINCRBY user:1000 visits 1 => 1  

  
  
	


 
  
  
