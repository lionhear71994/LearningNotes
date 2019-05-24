package com.lionheart.learning.entity;

import org.apache.ibatis.type.Alias;

//@Component("user")
@Alias(value = "user")
public class User {
    //@Id
    //@GeneratedValue(strategy=GenerationType.AUTO)
//    @Value("1")
    private Integer id;
//    @Value("LH")
    private String username;
//    @Value("113@163.com")
    private String email;
//    @Value("1")
    private SexEnum sex;

    public SexEnum getSex() {
        return sex;
    }

    public void setSex(SexEnum sex) {
        this.sex = sex;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}