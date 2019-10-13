### 线程生命周期
* NEW:新建线程还未调用start()
* RUNNABLE:运行中和准备运行统称为RUNNABLE
* BLOCKED:被其他锁阻塞
* WATING :需要其他线程唤醒
* TIME_WATING:wait(n),sleep(n)，时间到了自动进入RUNNABLE
* TERMINATED:执行完run()方法后进入此状态
### 死锁条件
互斥条件、请求与保持条件、不剥夺条件、循环等待条件
### 悲观锁与乐观锁
* 悲观锁：共享资源每次只给一个线程使用，其它线程阻塞，用完后再把资源转让给其它线程。Java中synchronized和ReentrantLock等独占锁就是悲观锁思想的实现。
* 乐观锁：CAS和版本号机制。
### syconized
* synchronized关键字可以保证被它修饰的方法或者代码块在任意时刻只能有一个线程执行；加到 static 静态方法和 synchronized(class)代码块上都是是给 Class 类上锁。synchronized 关键字加到实例方法上是给对象实例上锁。尽量不要使用 synchronized(String a) 因为JVM中，字符串常量池具有缓存功能！  
```java
//双重校验锁实现对象单例（线程安全）
public class Singleton {
    private volatile static Singleton uniqueInstance;
    private Singleton() {
    }
    public static Singleton getUniqueInstance() {
       //先判断对象是否已经实例过，没有实例化过才进入加锁代码
        if (uniqueInstance == null) {
            //类对象加锁
            synchronized (Singleton.class) {
                if (uniqueInstance == null) {
                    uniqueInstance = new Singleton();
                }
            }
        }
        return uniqueInstance;
    }
}
```
* synchronized和ReentrantLock：  
都是可重入锁；  
synchronized通过JVM底层实现，ReentrantLock通过lock()等方法API实现；  
ReentrantLock增加了一些高级功能，主要来说主要有三点：  
①等待可中断；     --lock.lockInterruptibly(),放弃等待改为做其他事情。  
②可实现公平锁；    --ReentrantLock(boolean fair)构造方法来实现，默认非公平。公平锁即先等待的线程先获得锁。    
③可实现选择性通知（锁可以绑定多个条件）。    --Condition接口实现,可更加灵活调度线程。
### volatile
* 禁止指令重排
* 多内存可见性
### 线程池
* 实现Runnable接口或Callable接口，用于ThreadPoolExecutor或ScheduledThreadPoolExecutor执行。
* execute() 方法用于提交不需要返回值的任务;submit() 方法用于提交需要返回值的任务。线程池会返回一个Future类型的对象。
* 建议通过ThreadPoolExecutor创建。