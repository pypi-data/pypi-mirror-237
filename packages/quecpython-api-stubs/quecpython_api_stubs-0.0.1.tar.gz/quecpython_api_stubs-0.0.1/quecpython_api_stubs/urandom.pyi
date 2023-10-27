"""
Function:
urandom模块提供了生成随机数的工具。

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/urandom.html
"""


def choice(obj: str) -> str:
    """随机生成对象obj中的元素，obj类型string。

    @obj：str类型
    @return：obj中随机某个元素，char
    """

def getrandbits(k: int) -> int:
    """随机产生一个在k(bits)范围内的十进制数。

    @k:int类型，表示范围（单位bit）
    @return:int类型，在k bits范围内的十进制随机数
    """

def randint(start: int, end: int) -> int:
    """随机生成一个start到end之间的整数。

    @start，int类型，区间最小值
    @end，int类型，区间最大值
    @return:int类型，在start到 end 之间的随机整数
    """

def random() -> float:
    """随机生成一个0到1之间的浮点数。

    @return:浮点数，在0到1之间。
    """

def randrange(start, end, step) -> int:
    """随机生成 start 到 end 间并且递增为 step 的正整数。

    @start:int类型，区间最小值
    @end:int类型，区间最大值
    @step:int类型，递增长度
    @return:int类型，在 start到 end 之间的随机整数
    """

def seed(sed:int):
    """指定随机数种子，通常和其它随机数生成函数搭配使用。

    @sed:int类型
    """

def uniform(start, end):
    """随机生成start到end范围内的浮点数。

    @start:任意实数类型，区间最小值
    @end:任意实数类型，区间最大值
    @return:浮点数类型，在start到end之间的随机数
    """
