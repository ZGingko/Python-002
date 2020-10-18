# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MoviespiderPipeline:
    def process_item(self, item, spider):        
        print("process_item")
        title = item['title']
        link = item['link']
        content = item['content']
        output = f'|{title}|\t|{link}|\t|{content}|\r\n'
        with open('./doubanmovie2.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
            # article.close()
        # print(item)
        return item
