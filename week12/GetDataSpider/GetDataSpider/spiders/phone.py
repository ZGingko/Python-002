import scrapy
from scrapy.selector import Selector
from GetDataSpider.config import common
from GetDataSpider.items import CommentItem


class PhoneSpider(scrapy.Spider):
    name = 'phone'
    allowed_domains = ['smzdm.com']

    def start_requests(self):
        yield scrapy.Request(
            url='https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/',
            callback=self.parse,
            headers=common.HEADERS
        )

    def parse(self, response):
        ul = Selector(response=response).xpath(
            '//*[@id="feed-main-list"]/li[position()<11]')
        for li in ul:
            item = CommentItem()
            link = li.xpath('./div/div[2]/h5/a/@href')[0].get()
            title = li.xpath('./div/div[2]/h5/a/text()')[0].get()
            item['phone'] = title
            item['alink'] = link
            item['user_comment'] = []
            yield scrapy.Request(
                url=link,
                meta={'item': item},
                callback=self.parse_detail)

    def parse_detail(self, response):
        item = response.meta['item']
        ul = Selector(response=response).xpath(
            '//*[@id="commentTabBlockNew"]/ul[1]/li')
        alink = Selector(response=response).xpath(
            '(//*[@class="pageCurrent"])[2]/../following-sibling::li[1]/a/@href').get()
        print(alink)

        for li in ul:
            user = li.xpath('./div[2]/div[1]/a/span/text()')[0].get()
            comment = li.xpath(
                './div[2]/div[@class="comment_conWrap"]/div[1]/p/span/text()').get()
            comment = ''.join(comment).strip()
            item['user_comment'].append((user, comment))
        if alink:
            yield scrapy.Request(url=alink, meta={'item': item}, callback=self.parse2)
        else:
            yield item
