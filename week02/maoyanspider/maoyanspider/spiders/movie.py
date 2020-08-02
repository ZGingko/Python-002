import scrapy
from maoyanspider.items import MaoyanspiderItem
from scrapy.selector import Selector


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://maoyan.com/films?showType=3']
    cookies = {'__mta': '188709399.1595764502994.1595764502994.1595764768326.2',
               'uuid_n_v': 'v1', 'uuid': 'D62230D0CF3611EABDA91DE1C2FF6305B6631D4EAD274DCA9B7099E9AD80DC61',
               'mojo-uuid': 'c0052bcd8b1aefe904a79e91bcab99b8',
               '_lxsdk_cuid': '1738af9f112c8-005435309de155-4353760-1fa400-1738af9f112c8',
               '_lxsdk': 'D62230D0CF3611EABDA91DE1C2FF6305B6631D4EAD274DCA9B7099E9AD80DC61',
               '_csrf': '2bd6ae3844deb199d95a2045b37e98f747286ea07ebd8f1ce2b3288d1534b213',
               'mojo-session-id': '{"id":"bff614afaee88dfeee2f5c79097c1dc3","time":1596376485944}',
               'mojo-trace-id': '1',
               'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2': '1595764503,1595772653,1596376486',
               'Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2': '1596376486',
               '__mta': '188709399.1595764502994.1595764768326.1596376486207.3',
               '_lxsdk_s': '173af7410f7-a5-c50-edc%7C%7C2'}

    def start_requests(self):
        url = MovieSpider.start_urls[0]
        yield scrapy.Request(url=url, cookies=MovieSpider.cookies, callback=self.parse)

    def parse(self, response):
        # print(response.text)
        movies = Selector(response=response).xpath(
            '//div[@class="movie-hover-info"]')[:10]
        print(movies)
        for movie in movies:
            movie_name = movie.xpath('./div[1]/span[1]/text()').extract_first()
            movie_type = movie.xpath(
                './div[2]/text()').extract()[1].strip().replace('\n', '').replace('\r', '')
            movie_date = movie.xpath(
                './div[4]/text()').extract()[1].strip().replace('\n', '').replace('\r', '')

            movie_item = MaoyanspiderItem()

            movie_item['movie_name'] = movie_name
            movie_item['movie_type'] = movie_type
            movie_item['movie_date'] = movie_date

            yield movie_item
