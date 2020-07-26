import scrapy
from maoyanspider.items import MaoyanspiderItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = MaoyanSpider.start_urls[0]
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.text)
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')[:10]
        print(movies)
        for movie in movies:
            movie_name = movie.xpath('./div[1]/span[1]/text()').extract_first()
            movie_type = movie.xpath('./div[2]/text()').extract()[1].strip().replace('\n', '').replace('\r', '')
            movie_date = movie.xpath('./div[4]/text()').extract()[1].strip().replace('\n', '').replace('\r', '')

            movie_item = MaoyanspiderItem()
            movie_item['movie_name'] = movie_name
            movie_item['movie_type'] = movie_type
            movie_item['movie_date'] = movie_date
            
            yield movie_item

