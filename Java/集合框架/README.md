### ArrayList扩容
```java
int DEFAULT_CAPACITY = 10;
int newCapacity = oldCapacity + (oldCapacity >> 1)
```
### Collections
* ArrayList:底层数组实现，查询快，增删慢。
* LinkedList:底层双向链表，增删快，查询慢。
* HashSet:基于HashMap，仅存储对象，hash原则来判断对象是否重复。
* HashMap:支持一个"null"key，多个"null"value。
