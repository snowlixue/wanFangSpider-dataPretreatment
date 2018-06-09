import scrapy

from wanfang.items import WanfangItem
from scrapy.selector import Selector
from scrapy import Request

#from scrapy import log

class WanfangSpider(scrapy.Spider):
    name = 'wanfang'
    allowed_domains = ["wanfangdata.com.cn"]
    start_urls = [
        'http://s.wanfangdata.com.cn/Paper.aspx?q=的&f=top&p=1'
    ]
    
    cookies = {}

    headers = {
        # 'Connection': 'keep - alive',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }

    meta = {
        'dont_redirect': True,
        'handle_httpstatus_list': [301, 302]
    }


    def start_requests(self):
        yield Request(self.start_urls[0], callback=self.parse, headers=self.headers, cookies=self.cookies, meta=self.meta) 

    def __init__(self):
        self.key = '的'
        self.count = 0
        self.url_1 = 'http://s.wanfangdata.com.cn/Paper.aspx?q='+ self.key +'&f=top&p=' 

    def parse(self, response):        
        sel = Selector(response)
        count = sel.xpath('/html/body/div[@class="content content-search clear"]/div[@class="right"]/div[@class="record-item-list"]/p[@class="pager"]/span[@class="page_link"]/text()').extract()
        page_count = int(count[0].split("/")[1])
        for i in range(1, page_count + 1):
            urls = self.url_1 + str(i)
            yield Request(urls, callback = self.parse_user_detail)

    def parse_user_detail(self, response):
        sel = Selector(response)
        url_s = sel.xpath('/html/body/div[@class="content content-search clear"]/div[@class="right"]/div[@class="record-item-list"]/div[@class="record-item"]/div[@class="left-record"]/div[@class="record-title"]/a[@class="title"]/@href').extract()
        for i in url_s:
            yield Request(i, callback = self.parse_page)

    def parse_page(self, response):
        sel = Selector(response)
        head = sel.xpath("/html/body/div[@class='fixed-width baseinfo clear']/div[@class='section-baseinfo']")
        body = sel.xpath("/html/body/div[@class='fixed-width-wrap fixed-width-wrap-feild']/div[@class='fixed-width baseinfo-feild']")
        item = WanfangItem()
        C_title = head.xpath("//h1/text()").extract()
        E_title = head.xpath("//h2/text()").extract()
        abstract = head.xpath("//div[@class='baseinfo-feild abstract']/div[@class='row clear zh']/div[@class='text']/text()").extract()
        C_author = body.xpath("//div[@class='row row-author']/span[@class='text']/a/text()").extract()
        E_author = body.xpath("//div[@class='row row-author']/span[@class='text']/span/text()").extract()
        periodical = body.xpath("//div[@class='row row-magazineName']/span[@class='text']/a/text()").extract()
        keywords = body.xpath("//div[@class='row row-keyword']/span[@class='text']/a/text()").extract()
        time = body.xpath("//div[last()]/span[@class='text']/text()").extract()[1]
        fund = body.xpath("//div[last()-1]/span[@class='text']/text()").extract()[1]
        
        item['abstract'] = ''.join(abstract)
        item['C_title'] = ''.join(C_title)
        item['E_title'] = ''.join(E_title)
        item['C_author'] = '、'.join(C_author)
        item['E_author'] = '、'.join(E_author)
        item['periodical'] =  '、'.join(periodical)
        item['keywords'] = '、'.join(keywords)
        item['time'] = ''.join(time)
        item['fund'] = ''.join(fund)
        item['link'] = ''.join(response.url)



        yield item
