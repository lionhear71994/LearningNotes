package com.lionheart.learning.mybatis;

import com.lionheart.learning.entity.User;
import org.springframework.stereotype.Repository;

@Repository
public interface MyBatisUserDao {

    public User getUser(int id);

    public int insertUser(User user);

}
