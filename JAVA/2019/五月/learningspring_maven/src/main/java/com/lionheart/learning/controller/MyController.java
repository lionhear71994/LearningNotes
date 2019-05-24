package com.lionheart.learning.controller;

import com.lionheart.learning.entity.SexEnum;
import com.lionheart.learning.entity.User;
import com.lionheart.learning.mybatis.MyBatisUserServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/mybatis")
public class MyController {

    @Autowired
    MyBatisUserServiceImpl myBatisUserService;

    @RequestMapping("/getUser")
    public User getWorker(int id){
        return myBatisUserService.getUser(id);
    }

    @RequestMapping("/insertUser")
    public Map<String,Object> insertUser(String username, String mail, int sex){
        User user = new User();
        user.setUsername(username);
        user.setEmail(mail);
        user.setSex(SexEnum.getEnumById(sex));
        int update = myBatisUserService.insertUser(user);
        Map<String,Object> result = new HashMap<>();
        result.put("success",update == 1);
        result.put("user",user);
        return result;
    }

}
