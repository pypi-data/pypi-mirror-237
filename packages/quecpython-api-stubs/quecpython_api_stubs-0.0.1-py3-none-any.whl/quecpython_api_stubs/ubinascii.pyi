"""
Function:
该模块实现了二进制数据与各种ASCII编码之间的转换(双向)。该模块实现相应CPython模块的子集，更多信息请参阅阅CPython文档：https://docs.python.org/3.5/library/binascii.html#module-binascii

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/ubinascii.html
"""


def a2b_base64(data: str):
    """解码base64编码的数据，会自动忽略输入中的无效字符。

    @data:字符串数据。
    @return:返回bytes对象。
    """

def b2a_base64(data: bytes):
    """以base64格式编码二进制数据。后面跟换行符，作为bytes对象。

    @data:字节数据。
    @return:返回编码数据(ascii)。
    """

def hexlify(data: bytes, sep: str = ''):
    """将二进制数据转换为十六进制字符串表示。

    @data:字节数据。
    @sep:分隔字符，默认是空字符即无分隔。
    @return:字符串数据。
    """


def unhexlify(data: str):
    """将十六进制形式的字符串转换成二进制形式的字符串表示。

    @data:字符串数据。
    @return:字节数据。
    """
