参考资料：[Docker命令](https://juejin.im/post/5d0781f56fb9a07f014ef6be)  
搜索镜像  
docker search [镜像名]  
下载镜像  
docker pull java:8  
列出镜像  
docker images  
删除镜像  
docker image rm [镜像名/id]     -f强制  

新建并启动容器
docker run -p 80:80 --name nginx -d nginx:1.17.0  
-d选项：表示后台运行  
--name选项：指定运行后容器的名字为nginx,之后可以通过名字来操作容器  
-p选项：指定端口映射，格式为：hostPort:containerPort  

列出容器  
docker ps(运行中容器） -a(全部容器)  
停止容器  
docker stop [镜像名/id]  
强制停止容器
docker kill  [镜像名/id]  
启动已停止的容器
docker start  [镜像名/id]    


