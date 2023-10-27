"""
Function:
系统相关功能

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/sys.html
"""


argv: list = ...  # 当前程序启动的可变参数列表
byteorder: str = ...  # 字节顺序 ("little"-小端， "big"-大端)

# 返回当前microPython版本信息。
# 对于MicroPython，它具有以下属性：
#   name - 字符串“ micropython”
#   version - 元组（主要，次要，微型），例如（1、7、0）
#   _mpy - mpy文件的版本信息
implementation: str = ...

# 本机整数类型可以在当前平台上保留的最大值。
# 如果它小于平台最大值，则为MicroPython整数类型表示的最大值（对于不支持长整型的MicroPython端口就是这种情况）。
maxsize: int = ...

modules: dict = ...  # 以字典形式返回当前Python环境中已经导入的模块。
platform: str = ...  # MicroPython运行的平台。
stdin = ...  # 标准输入（默认是USB虚拟串口，可选其他串口）。
stdout = ...  # 标准输出（默认是USB虚拟串口，可选其他串口）。
version: str = ...  # MicroPython版本，字符串格式。
version_info: tuple = ...  # MicroPython版本，整数元组格式。

def exit(retval: int = 0):
    """使用给定的参数退出当前程序。

    @retval:int型，退出参数
    @raise:该函数会引发 SystemExit退出。如果给定了参数，则将其值作为参数赋值给SystemExit。
    """

def print_exception(exc, file=stdout):
    """打印异常到文件对象，默认是sys.stdout，即输出异常信息的标准输出。

    @exc:exception对象
    @file:指定输出文件，默认为sys.stdout
    """
