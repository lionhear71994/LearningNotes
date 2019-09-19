1、防火墙设置
查看开放端口:	iptables -L -n
查看防火墙状态:	firewall-cmd --state/service iptable status
开放22端口：	iptables -A INPUT -p tcp --dport 22 -j ACCEPT
				iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT
				***service iptables save***
				vim /etc/sysconfig/iptables
2、查询
查看已安装软件：	rpm -qa | grep "xxx"
					yum list installed | grep "xxx" 
查看软件位置：	rpm -ql "xxx"

显示所有进程的消息:		ps -ef | grep xxx

查看所有服务: systemctl | grep running

查看启动项：	systemctl list-unit-files

查看所有process: 		top

查看CentOS版本：	cat /etc/redhat-release

3、安装卸载
yum remove xxx

wget http://mirror.bit.edu.cn/apache/tomcat/tomcat-9/v9.0.20/bin/apache-tomcat-9.0.20-deployer.tar.gz
tar -zxvf apache-tomcat-9.0.0.M18.tar.gz

删除目录及其中文件：	rm -rf 目录名字

4、启动停止
启动和停止Tomcat:	进入tomcat目录/bin，然后./startup.sh	./shutdown.sh

systemctl enable [unit type] 	设置服务开机启动
systemctl disable [unit type] 	设备服务禁止开机启动

杀死进程:               kill -s 9 xxxx
后台运行:	nohup &

进入redis:	redis-cli
			keys *
			
运行可执行Jar：	java -jar XXX.jar  
				java -jar XXX.jar & (&表示后台运行)
				nohup java -jar XXX.jar & (nohup当账户退出或终端关闭时，程序依然继续运行)  
				

				

