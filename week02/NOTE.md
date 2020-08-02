### 学习笔记
#### 安装MySql

1）安装MySQL YUM资源库  
[root@localhost ~]# ` yum localinstall https://dev.mysql.com/get/mysql57-community-release-el7-8.noarch.rpm`
 
2）安装MySQL 5.7  
[root@localhost ~]# ` yum install -y mysql-community-server`
 
3）启动MySQL服务器和MySQL的自动启动  
[root@localhost ~]# `systemctl start mysqld.service`  
[root@localhost ~]# `systemctl enable mysqld.service`
 
4）密码问题
由于MySQL从5.7开始不允许首次安装后使用空密码进行登录！为了加强安全性，系统会随机生成一个密码以供管理员首次登录使用，
这个密码记录在`/var/log/mysqld.log`文件中，使用下面的命令可以查看此密码：  
[root@localhost ~]# `cat /var/log/mysqld.log|grep 'A temporary password'`  
2018-01-20T02:32:20.210903Z 1 [Note] A temporary password is generated for root@localhost: `DOqInortw9/<`
 
最后一行冒号后面的部分`DOqInortw9/<`就是初始密码。
使用此密码登录MySQL:
[root@localhost ~]# mysql -uroot -p


5）使用随机生产的密码登录到服务端后，必须马上修改密码，不然会报如下错误：  
mysql> `show databases;`  
ERROR 1820 (HY000): You must reset your password using ALTER USER statement before executing this statement.


有两种方法解决上面的报错（如下的123456是修改后的密码）：  
mysql> `set password=password("123456");`  
或者  
mysql> `alter user 'root'@'localhost' identified by '123456';`
 
刷新权限  
mysql> flush privileges;
 
 ***

如果上面在执行 `set password=password("123456");`命令后出现下面的报错：  
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements
 
解决办法：  
这个与Mysql 密码安全策略`validate_password_policy`的值有关，`validate_password_policy `可以取0、1、2三个值：  
0 or LOW       Length  
1 or MEDIUM    Length; numeric, lowercase/uppercase, and special characters  
2 or STRONG    Length; numeric, lowercase/uppercase, and special characters; dictionary 
 
默认的数值是1，符合长度，且必须含有数字，小写或大写字母，特殊字符。  
所以刚开始设置的密码必须符合长度，且必须含有数字，小写或大写字母，特殊字符。
 
有时候，只是为了自己测试，不想密码设置得那么复杂，譬如说，我只想设置root的密码为123456。
必须修改两个全局参数：  
mysql> `set global validate_password_policy=0;`  
Query OK, 0 rows affected (0.00 sec)
 
mysql> `set global validate_password_length=1;`  
Query OK, 0 rows affected (0.00 sec)
 
修改上面两个参数后，就可以解决这个报错了。
***
注意一点：
mysql5.7之后的数据库里`mysql.user`表里已经没有`password`这个字段了，`password`字段改成了`authentication_string`。
所以修改密码的命令如下：
 
mysql> `update mysql.user set authentication_string=password('123456') where user='root';`  
Query OK, 1 row affected, 1 warning (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 1
 
mysql> `flush privileges;`  
Query OK, 0 rows affected (0.00 sec)





> 参考链接：https://juejin.im/post/6844903926068674574