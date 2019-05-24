//package com.lionheart.learning;
//
//import com.lionheart.learning.config.MyConfiguration;
//import com.lionheart.learning.entity.User;
//import org.junit.Test;
//import org.junit.runner.RunWith;
//import org.slf4j.Logger;
//import org.slf4j.LoggerFactory;
//import org.springframework.boot.test.context.SpringBootTest;
//import org.springframework.context.ApplicationContext;
//import org.springframework.context.annotation.AnnotationConfigApplicationContext;
//import org.springframework.test.context.junit4.SpringRunner;
//
//@RunWith(SpringRunner.class)
//@SpringBootTest
//public class SpringLearningApplicationTests {
//
//    private static Logger log = LoggerFactory.getLogger(SpringLearningApplicationTests.class);
//
//    @Test
//    public void contextLoads() {
//        ApplicationContext context = new AnnotationConfigApplicationContext(MyConfiguration.class);
//        User user = (User)context.getBean("user");
//        log.debug(user.getUsername() + " " + user.getEmail());
//    }
//
//}
