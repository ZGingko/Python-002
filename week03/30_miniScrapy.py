import requests
from lxml import etree
from queue import Queue
import threading
import json
from fake_useragent import UserAgent


class CrawlThread(threading.Thread):
    '''爬虫类'''

    def __init__(self, thread_id, queue):
        super().__init__()
        self.thread_id = thread_id
        self.queue = queue

    def run(self):
        print(f'启动线程：{self.thread_id}')
        self.scheduler()
        print(f'结束线程：{self.thread_id}')

    def scheduler(self):
        while True:
            if self.queue.empty():
                break
            else:
                page = self.queue.get()
                print(f'下载线程为：{self.thread_id}，下载页面：{page}')
                url = f'https://book.douban.com/top250?start={page*25}'
                ua = UserAgent(verify_ssl=False)
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
                }
                try:
                    response = requests.get(url, headers=headers)
                    dataQueue.put(response.text)
                except Exception as e:
                    print('下载出现异常', e)


class ParseThread(threading.Thread):
    '''解析类'''

    def __init__(self, thread_id, queue, file):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.queue = queue
        self.file = file

    def run(self):
        print(f'启动线程：{self.thread_id}')
        while not flag:
            try:
                item = self.queue.get(False)  # 参数为false时，队列为空会抛异常
                if not item:
                    continue
                self.parse_data(item)
                self.queue.task_done()
            except Exception as e:
                pass
                # print('解析出现异常', e)
        print(f'结束线程：{self.thread_id}')

    def parse_data(self, item):
        try:
            html = etree.HTML(item)
            books = html.xpath('//div[@class="pl2"]')
            for book in books:
                try:
                    title = book.xpath('./a/text()')
                    link = book.xpath('./a/@href')
                    print(title)
                    response = {
                        'title': title,
                        'link': link
                    }
                    json.dump(response, fp=self.file, ensure_ascii=False)
                except Exception as e:
                    print('book error: ', e)
        except Exception as e:
            print('page error: ', e)


dataQueue = Queue()
flag = False

if __name__ == '__main__':
    output = open('book_ig.json', 'a', encoding='utf-8')

    pageQueue = Queue(20)
    for page in range(10):
        pageQueue.put(page)

    crawl_threads = []
    crawl_name_list = ['crawl_1', 'crawl_2', 'crawl_3']
    for thread_id in crawl_name_list:
        thread = CrawlThread(thread_id, pageQueue)
        thread.start()
        crawl_threads.append(thread)

    parse_threads = []
    parse_name_list = ['parse_1', 'parse_2', 'parse_3']
    for thread_id in parse_name_list:
        thread = ParseThread(thread_id, dataQueue, output)
        thread.start()
        parse_threads.append(thread)

    for t in crawl_threads:
        t.join()
    flag = True

    for t in parse_threads:
        t.join()

    output.close()
    print('退出主线程')
