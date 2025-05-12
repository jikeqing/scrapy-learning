# 1.推导式 ： 可以用来生成列表、集合、字典
# l = [i for i in range(10)]
# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# scores = [[None] * len(courses) for _ in range(len(names))]
# print(scores)
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
#         print(scores)


# 2.heapq模块
"""
heapq模块提供了堆队列算法，也叫优先队列算法。
该模块提供了以下函数：
heapq.heapify(x)  # 堆化列表x
heapq.heappush(heap, item)  # 将item添加到堆中
heapq.heappop(heap)  # 弹出堆中最小的元素
heapq.heappushpop(heap, item)  # 将item添加到堆中，然后弹出最小的元素
heapq.merge(*iterables, key=None, reverse=False)  # 合并多个已排序的迭代器
heapq.nlargest(n, iterable, key=None)  # 返回前n个最大的元素  iterable是可迭代对象, key=函数
heapq.nsmallest(n, iterable, key=None)  # 返回前n个最小的元素
heapq.heapify(x)  # 堆化列表x
"""

"""
从列表中找出最大的或最小的N个元素
堆结构(大根堆/小根堆)
"""
# import heapq
#
# list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(3, list1))
# print(heapq.nlargest(2, list2, key=lambda x: x['price']))
# print(heapq.nlargest(2, list2, key=lambda x: x['shares']))

# itertools模块
"""
itertools 模块提供了用于操作迭代器的函数。
该模块提供了以下函数：
itertools.count(start=0, step=1)  # 创建一个无限迭代器
itertools.cycle(iterable)  # 创建一个无限循环迭代器
itertools.repeat(object, times=None)  # 创建一个重复的迭代器
itertools.chain(*iterables)  # 将多个迭代器连接在一起
itertools.islice(iterable, start, stop[, step])  # 切片迭代器
itertools.groupby(iterable, key=None)  # 分组迭代器
itertools.product(*iterables, repeat=1)  # 笛卡尔积
itertools.permutations(iterable, r=None)  # 全排列
itertools.combinations(iterable, r)  # 组合
itertools.combinations_with_replacement(iterable, r)  # 组合，允许重复

"""
# import itertools
#
#
# for i in itertools.count(10,2):
#     print(i)

# for i in itertools.cycle('ABC'):
#     print(i)

# for i in itertools.repeat('ABC', 10):
#     print(i)

# for i in itertools.chain('ABC', 'DEF'):
#     print(i)

# for i in itertools.islice(itertools.count(10), 5):
#     print(i)
#
# for i in itertools.groupby('AAAABBBCCDAABBB'):
#     # print(i)
#     print(list(i))

# for i in itertools.product('ABCD', 'EFG','HI'):
#     print(i)

# for i in itertools.permutations('ABCD', 2):
#     print(i)

# for i in itertools.combinations('ABCD', 2):
#     print(i)

# for i  in itertools.combinations_with_replacement('ABCD', 2):
#     print(i)


# 4.collections模块
"""
collections模块提供了许多有用的集合类。
该模块提供了以下类：
collections.Counter  # 计数器
    dict的子类， 键是元素，值是元素的计数，
    他的most_common() 方法可以帮助我们获取出现频率最高的元素
collections.defaultdict  # 默认字典
    类似于字典，但是可以通过默认的工厂函数来获得键对应的默认值，向比较字典中的setdefault（）方法，这种做法更加高效
collections.OrderedDict  # 有序字典
    dict的子类，它记录了键值对插入的顺序，看起来既有字典的行为，也由链表的行为
collections.deque  # 双端队列
    列表的替代实现，python中的列表底层是基于数组来实现的
    而deque底层是双向链表因此当你需要在头尾添加和删除元素时 ，
    deque会表现出更好的性能，渐进时间复杂都为O(1)
collections.namedtuple  # 命名元组
    它是一个类工厂，接受类型的名称和属性列表来创建一个类
collections.ChainMap  # 链接多个字典
collections.UserDict  # 用户字典
collections.UserList  # 用户列表
collections.UserString  # 用户字符串
collections.abc  # 抽象基类

"""
# import collections
#
# time = collections.defaultdict(int)
# time['a'] = 1
# time['b'] = 2
# time['c'] = 3
# time['d'] = 4
# time['f'] = "zjhamg"
# print(time)

# 5.数据结构与算法
"""
算法：解决问题的方法和步骤
评价算法的好坏：渐进时间复杂度和渐进空间复杂度。
时间复杂度：算法执行所需的时间与输入数据规模之间的关系。
空间复杂度：算法执行所需的存储空间与输入数据规模之间的关系。
渐进时间复杂度用大O表示法表示。
大O表示法：表示算法的渐进时间复杂度的上界。
O(1) 常数阶 表示算法的执行时间与输入数据规模无关 例如：布隆过滤器/哈希存储
O(log n) 对数阶  算法的执行时间随着输入规模的增加以对数形式增长，增长速度较慢
        例如 二分查找
O(n) 线性阶  算法的执行时间与输入规模成正比，输入规模每增加一倍，执行时间也增加一倍，
        例如遍历
O(n*log2^n) 线性对数阶 算法的执行时间是输入规模乘以对数的增长
        例如：归并排序，快速排序
O(n^2) 平方阶 算法执行时间与输入规模的平方成正比，输入规模每增加一倍，执行时间增加四倍
        例如：冒泡排序，选择排序，插入排序
O(n^3) 立方阶 算法执行时间与输入规模的立方成正比，输入规模每增加一倍，执行时间增加八倍
        例如：Floyd 算法 /矩阵乘法运算
O(2^n) 指数阶 算法执行时间随着输入规模的增加呈指数增长，输入规模每增加一倍，执行时间增加两倍，增长非常快
        例如：汉诺塔
O(n!) 阶乘阶 算法执行时间随着输入规模的增加以阶乘形式增长，增长速度极快，
        例如：旅行商问题
"""

# class MyKey:
#     def __init__(self, key):
#         self.key = key
#
#     def __hash__(self):
#         return hash(self.key)
#
#     def __eq__(self, other):
#         return self.key == other.key
#
# key1 = MyKey("a")
# key2 = MyKey("a")
# key3 = MyKey("b")
#
# my_dict = {key1: "value1", key3: "value2"}
# print(my_dict)
# print(my_dict[key2])  # 输出：value1


fish = 6
while True:
    total = fish
    enough = True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            enough = False
            break
    if enough:
        print(fish)
        break
    fish += 5
