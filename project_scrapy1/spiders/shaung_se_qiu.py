import scrapy


class ShaungSeQiuSpider(scrapy.Spider):
    name = "shaung_se_qiu"
    allowed_domains = ["sina.com.cn"]
    start_urls = ["https://view.lottery.sina.com.cn/lotto/pc_zst/index?lottoType=ssq&actionType=chzs&type=50&dpc=1"]

    def parse(self, response,**kwargs):
        ball_lists = response.xpath('//*[@id="cpdata"]/tr')
        id = 1
        for ball_list in ball_lists:
            qi_hao = ball_list.xpath('.//td[1]/text()').extract_first()
            red_ball = ball_list.xpath('.//td[@class="chartball01" or @class="chartball20"]//text()').extract()
            blue_ball = ball_list.xpath('.//td[@class="chartball02"]/text()').extract_first()
            # print(f"id:::{id}")
            # print(f"qi_hao:::{qi_hao},  red_ball:::{red_ball},  blue_ball:::{blue_ball}")
            # print("=="*50)
            yield {
                "id": id,
                "qi_hao": qi_hao,
                "red_ball": red_ball,
                "blue_ball": blue_ball
            }
            id += 1
