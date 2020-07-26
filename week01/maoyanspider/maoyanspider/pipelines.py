# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class MaoyanspiderPipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_date = item['movie_date']
        item_list = [movie_name, movie_type, movie_date]
        movie_pd = pd.DataFrame(data=item_list)
        movie_pd.to_csv('./maoyan_top10.csv', index=False, mode='a', header=False)
        return item
