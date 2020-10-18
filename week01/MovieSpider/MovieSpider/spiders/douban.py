import scrapy
from MovieSpider.items import MoviespiderItem
from bs4 import BeautifulSoup
from scrapy.selector import Selector


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['moive.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        for i in range(2):
            url = f'https://movie.douban.com/top250?start={i*25}'
            yield scrapy.Request(url=url, callback=self.parse_by_selector)
    
    def parse_by_selector(self, response):
        print(response.url)
        items = []
        movies = Selector(response=response).xpath('//div[@class="hd"]')
        for movie in movies:
            # print(movie.xpath('text()'))
            title = movie.xpath('./a/span/text()')
            link = movie.xpath('./a/@href')
            movie_item = MoviespiderItem()
            movie_item['title'] = title.extract_first()
            movie_item['link'] = link.extract_first()
            # movie_item['content'] = movie_item['title']
            # yield movie_item
            print(link.extract_first())
            yield scrapy.Request(url=link.extract_first(), callback=self.parse_detail_by_selector, meta={'item': movie_item}, dont_filter=True)

    def parse_detail_by_selector(self, response):
        print("parse_detail_by_selector")
        movie_item = response.meta['item']
        # content_div = Selector(response=response).xpath('//div[@class="related-info"]')[0]
        # print("content_div" + content_div)
        # movie_item['content'] = content_div.xpath('./text()')
        movie_item['content'] = movie_item['title']
        yield movie_item



    def parse_by_selector1(self, response):
        print(response.url)
        items = []
        movies = Selector(response=response).xpath('//div[@class="hd"]')
        for movie in movies:
            title = movie.xpath('./a/span/text()')
            link = movie.xpath('./a/@href')
            movie_item = MoviespiderItem()
            movie_item['title'] = title.extract_first()
            movie_item['link'] = link.extract_first()
            yield scrapy.Request(url=link.extract_first(), callback=self.parse_detail_by_selector, meta={'item': movie_item})
            # movie_item['content'] = "empty"
            # yield movie_item
            # items.append(movie_item)
        # return items
        
            # print('-------------------------')
            # print(title)
            # print(link)
            # print('-------------------------')
            # print(title.extract())
            # print(link.extract())
            # print(title.extract_first())
            # print(link.extract_first())
            # print(title.extract_first().strip())
            # print(link.extract_first().strip())

    def parse(self, response):
        items = []
        soup = BeautifulSoup(response.text, 'html.parser')
        title_list = soup.find_all('div', attrs={'class': 'hd'})
        for item in title_list:
            movie_item = MoviespiderItem()
            title = item.find('a').find('span',).text
            link = item.find('a').get('href')
            movie_item['title'] = title
            movie_item['link'] = link
            # items.append(movie_item)
            yield scrapy.Request(url=link, meta={'item': movie_item}, callback=self.parse_detail)
        # return items

    def parse_detail(self, response):
        movie_item = response.meta['item']
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find(
            'div', attrs={'class': 'related-info'}).get_text().strip()
        movie_item['content'] = content
        yield movie_item
