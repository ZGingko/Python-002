学习笔记
创建虚拟环境：python -m venv env_path
激活虚拟环境：env_path\Scripts\activate.bat; linux系统执行：source env_path/bin/activate
创建新的爬虫项目：
1、scrapy startproject spider_name, 
2、cd spider_project_name, 
3、scrapy genspider spider_name,
4、spider_name.py实现爬取逻辑，items.py实现爬取内容映射，piplines.py实现爬取内容输出
5、scrapy crawl spider_name，执行爬虫