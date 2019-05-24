//package com.lionheart.learning.controller;
//
//import com.lionheart.learning.repo.ProductRepository;
//import com.lionheart.learning.entity.User;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.stereotype.Controller;
//import org.springframework.web.bind.annotation.*;
//
//@Controller
//@RequestMapping(value = "/product")
//public class ProductController {
//
//    @Autowired
//    private ProductRepository productRepository;
//
//    @RequestMapping(value = "/addsingle")
//    public @ResponseBody String addSingle(@RequestParam(value = "name") String name,@RequestParam(value = "type") String type
//            ,@RequestParam(value = "count",defaultValue = "999") int count,@RequestParam(value = "price") float price){
//        User p  =new User();
//        p.setUsername(name);
//        p.setType(type);
//        p.setCount(count);
//        p.setPrice(price);
//        productRepository.save(p);
//        return "Saved";
//    }
//
//
//    @RequestMapping(value = "/getall",method= RequestMethod.GET)
//    public @ResponseBody Iterable<User> getAll(){
//        return productRepository.findAll();
//    }
//
//    @RequestMapping(value = "/delsingle")
//    public @ResponseBody String delSingle(@RequestParam(value = "id") int id){
//        productRepository.deleteById(id);
//        return "del success";
//    }
//}
