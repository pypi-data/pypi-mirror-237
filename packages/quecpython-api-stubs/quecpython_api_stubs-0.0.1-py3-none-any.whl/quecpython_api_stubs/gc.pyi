"""
Function:
gc模块实现内存垃圾回收机制，该模块实现了CPython模块相应模块的子集。更多信息请参阅CPython文档：gc

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/gc.html
"""


def enable():
    """启用自动回收内存碎片机制。"""

def disable():
    """禁用自动回收内存碎片机制。"""

def isenabled():
    """查询是否启动了自动回收内存碎片机制。

    @return:True-已启动自动回收内存碎片机制，False-未启动自动回收内存碎片机制。
    """

def collect():
    """主动回收内存碎片。"""

def mem_alloc():
    """查询已申请的内存大小。

    @return:返回已申请的内存大小，单位字节。
    """

def mem_free():
    """查询剩余可用的内存大小。

    @return:返回剩余可用的内存大小，单位字节。
    """
