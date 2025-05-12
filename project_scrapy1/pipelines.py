# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

"""
### csv 格式写入
"""
# class ProjectScrapy1Pipeline:
#     def __init__(self):
#         self.f = None
#     def open_spider(self, spider):   # 引擎中对“管道（pipelines）”的一个设计
#         self.f = open('lottery.csv', 'r+', encoding='utf-8')
#         self.f.write('id,期号,红球,蓝球\n')
#         print("开始写入")
#
#
#
#     def close_spider(self, spider):
#         self.f.close()
#         print("写入完成")
#
#
#     # item 数据
#     # process 处理
#     # process_item 处理数据
#     def process_item(self, item, spider):
#
#         red_ball = '__'.join(item['red_ball'])
#         self.f.write(f"{item['id']},{item['qi_hao']},{red_ball},{item['blue_ball']} \n")
#         print('ok')
#         return item


"""
### mysql 写入
"""


class ProjectScrapy1Pipeline_1:
    def __init__(self):
        self.con = None

    def open_spider(self, spider):  # 引擎中对“管道（pipelines）”的一个设计
        # 1.建立连接
        self.con = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='Zhou0820*',
            database='employees'
        )

        print("开始写入")

    def close_spider(self, spider):
        self.con.close()
        print("写入完成")

    # item 数据
    # process 处理
    # process_item 处理数据
    def process_item(self, item, spider):
        try:
            # 2.设置游标
            curses = self.con.cursor()

            # 3.写入数据
            sql = "insert into shuang_se_qiu(id,qi_hao,red_ball,blue_ball) values (%s,%s,%s,%s)"
            context = '__'.join(item['red_ball'])
            curses.execute(sql, (item['id'], item['qi_hao'], context, item['blue_ball']))

            # 4，提交事物
            self.con.commit()

        except Exception as e:
            print(e)
            # 5.如果报错，回滚
            self.con.rollback()
