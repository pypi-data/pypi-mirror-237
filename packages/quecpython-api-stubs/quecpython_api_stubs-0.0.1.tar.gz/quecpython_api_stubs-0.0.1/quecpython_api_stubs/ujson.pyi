"""
Function:
ujson模块实现在Python对象和JSON数据格式之间进行转换的功能。该模块实现相应CPython模块的子集。更多信息请参阅CPython文档：https://docs.python.org/3.5/library/json.html#module-json

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/ujson.html
"""


def dump(obj, stream):
    """序列化obj对象转化成JSON字符串，并将其写入到给定的stream中。

    @obj:Python对象，需要转换成JSON字符串的数据对象。
    @stream:数据流对象，转换成JSON字符串后写入的位置。
    """

def dumps(obj):
    """将Python对象转换成JSON字符串。

    @obj:Python对象，需要转换成JSON字符串的数据对象。
    @return:返回JSON字符串。
    """

def load(stream):
    """解析给定的数据stream，将其解析为JSON字符串并反序列化成Python对象，最终将对象返回。

    @stream:数据流对象，能够读取JSON字符串的数据流对象。
    @return:返回Python对象。
    """

def loads(string):
    """解析JSON字符串string并返回一个Python对象。

    @string:JSON字符串。
    @返回Python对象。
    """
