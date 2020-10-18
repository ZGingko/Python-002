DATABASE = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'gingko147',
    'database': 'learndb',
    'charset': 'utf8mb4'
}

SQL_DELETE_TABLE = "DROP TABLE IF EXISTS `t_phone_comments`;"

SQL_CREATE_TABLE = """
CREATE TABLE `t_phone_comments` (
  `Fid` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '评论id',
  `Fphone_title` varchar(255) NOT NULL COMMENT '手机标题',
  `Falink` varchar(255) DEFAULT NULL COMMENT '手机页面链接',
  `Fuser_name` varchar(255) NOT NULL COMMENT '用户名',
  `Fcomment` text NOT NULL COMMENT '评论',
  `Fsentiments` float NOT NULL COMMENT '情感',
  `Fcreate_time` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`Fid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""
# SQL_INIT_TABLE = "DELETE FROM comments;"
SQL_INSERT = """
INSERT INTO t_phone_comments
(`Fphone_title`, `Falink`, `Fuser_name`, `Fcomment`, `Fsentiments`, `Fcreate_time`)
VALUE
('{}', '{}', '{}', '{}', '{}', now());
"""

HEADERS = {
    'Cookie': 'IDE=AHWqTUnEZCZgekpu6JJbamXRABqVdqCYUUvjE5dceXcS_ZiHEW2ar83Ue4iPzEeX6Zk; DSID=NO_DATA',
}
