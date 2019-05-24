package com.lionheart.learning.mybatis;

import com.lionheart.learning.entity.User;


public interface MyBatisUserService {

    public User getUser(int id);

    public int insertUser(User user);
}
