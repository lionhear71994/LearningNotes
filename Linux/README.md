
查看开放端口:	iptables -L -n
查看防火墙状态:	firewall-cmd --state/service iptable status
开放22端口：	iptables -A INPUT -p tcp --dport 22 -j ACCEPT
				iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT
				***service iptables save***
				vim /etc/sysconfig/iptables
				
查看已安装软件：	rpm -qa | grep "xxx"
					yum list installed | grep "xxx" 
查看软件位置：	rpm -ql "xxx"

yum remove xxx

启动和停止Tomcat:	进入tomcat目录/bin，然后./startup.sh	./shutdown.sh

wget http://mirror.bit.edu.cn/apache/tomcat/tomcat-9/v9.0.20/bin/apache-tomcat-9.0.20-deployer.tar.gz
tar -zxvf apache-tomcat-9.0.0.M18.tar.gz

删除目录及其中文件：	rm -rf 目录名字

显示所有进程的消息:		ps -ef | grep xxx
杀死进程:               kill -s 9 xxxx
后台运行:	nohup &

进入redis:	redis-cli
			keys *
			
运行可执行Jar：	java -jar XXX.jar  
				java -jar XXX.jar & (&表示后台运行)
				nohup java -jar XXX.jar & (nohup当账户退出或终端关闭时，程序依然继续运行)  
				
