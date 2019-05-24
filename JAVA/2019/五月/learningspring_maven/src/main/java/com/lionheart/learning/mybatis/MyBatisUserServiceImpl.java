package com.lionheart.learning.mybatis;

import com.lionheart.learning.entity.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Isolation;
import org.springframework.transaction.annotation.Transactional;

@Service
public class MyBatisUserServiceImpl implements MyBatisUserService {

    //@Qualifier("initDao")
    @Autowired
    private MyBatisUserDao userDao;


    @Override
    public User getUser(int id) {
        return userDao.getUser(id);
    }

    @Override
    @Transactional(isolation = Isolation.READ_COMMITTED,timeout = 1)
    public int insertUser(User user) {
        return userDao.insertUser(user);
    }
}
