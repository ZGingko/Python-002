# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings
from maoyanspider.helper import ConnDB

# dbInfo = {
#     'host': '192.168.1.103',
#     'port': 3306,
#     'user': 'root',
#     'password': 'root123',
#     'db': 'learn_python'
# }

class MaoyanspiderPipeline:
    def __init__(self):
        settings = get_project_settings()
        dbInfo = {}
        dbInfo['host'] = settings.get('MYSQL_HOST')
        dbInfo['port'] = settings.get('MYSQL_PORT')
        dbInfo['user'] = settings.get('MYSQL_USER')
        dbInfo['password'] = settings.get('MYSQL_PASSWORD')
        dbInfo['db'] = settings.get('MYSQL_DB')
        self.conn = ConnDB(dbInfo)

    def process_item(self, item, spider):
        try:
            print('process_item')
            # print(self.conn)
            # movie_name = item['movie_name']
            # movie_type = item['movie_type']
            # movie_date = item['movie_date']
            # item_list = [movie_name, movie_type, movie_date]
            # movie_pd = pd.DataFrame(data=item_list)
            # movie_pd.to_csv('./maoyan_top10.csv', index=False, mode='a', header=False)
            self.conn.insert(item)
            return item
        except Exception as e:
            print(e)
