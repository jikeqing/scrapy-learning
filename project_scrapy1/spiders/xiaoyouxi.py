import scrapy
# 新建一个类，继承自scrapy.Spider
class XiaoyouxiSpider(scrapy.Spider):
    name = "xiaoyouxi"  # 定义爬虫名
    allowed_domains = ["4399.com"]  # 允许的域名
    start_urls = ["https://4399.com"]  # 爬虫入口，与该域名无关的会被忽略

    def parse(self, response):
        # response.xpath()  # 直接使用xpath解析，无需导包
        game_list = response.xpath('//*[@id="skinbody"]/div[10]/div[1]/div[1]/ul/li')
        id = 1
        for game in game_list:
            # 这里是scrapy 拿到的数据是由scrapy封装的xpath ，提取的是一个selecter
            game_name = game.xpath('./a/text()').extract_first()  # extract_first()
            # yield 可以在不打断程序运行的情况下， 将数据返回到scrapy框架中，
            # spider must return request、item、None
            # request 请求对象
            # item 数据
            # None 不返回数据
            # 数据会经过引擎，引擎会传递到管道
            yield {id: game_name}
            id += 1

