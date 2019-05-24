package com.lionheart.learning;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication()
@MapperScan(basePackages = "com.lionheart.learning.mybatis")
public class SpringLearningApplication {

//    @Autowired
//    SqlSessionFactory sqlSessionFactory;
//    @Autowired
//    PlatformTransactionManager transactionManager;

//    @PostConstruct
//    public void viewTransactionManager(){
//        System.out.println(transactionManager.getClass().getName());
//    }

    public static void main(String[] args) {
        SpringApplication.run(SpringLearningApplication.class, args);
        //getBean();

    }



//    @Bean
//    public MapperFactoryBean<MyBatisUserDao> initDao(){
//        MapperFactoryBean<MyBatisUserDao> mapperFactoryBean = new MapperFactoryBean<>();
//        mapperFactoryBean.setMapperInterface(MyBatisUserDao.class);
//        mapperFactoryBean.setSqlSessionFactory(sqlSessionFactory);
//        return mapperFactoryBean;
//    }

//    private static void getBean(){
//
//        User user = new User();
//    }

}
