"""
Function:
math模块提供数学运算函数。该模块实现相应CPython模块的子集。更多信息请参阅阅CPython文档：https://docs.python.org/3.5/library/math.html#module-math

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/math.html
"""

def pow(x, y):
    """返回x的y次方

    @x:任意实数类型
    @y:任意实数类型
    @return:float,x的y次方
    """

def acos(x):
    """返回x的反余弦弧度值

    @x:任意实数类型，是-1~1之间的数，包括-1和1，如果小于-1或者大于1，会产生错误。
    @return:float,x的反余弦弧度值
    """

def asin(x):
    """返回x的反正弦弧度值

    @x:任意实数类型，是-1~1之间的数，包括-1和1，如果小于-1或者大于1，会产生错误。
    @return:float,x的反正弦弧度值
    """

def atan(x):
    """返回x的反正切弧度值

    @x:任意实数类型
    return:float,x的反正切弧度值
    """

def atan2(x, y):
    """返回给定的X及Y坐标值的反正切值

    @x:任意实数类型
    @y:任意实数类型
    @return:float,坐标 (x,y)的反正切值
    """

def ceil(x):
    """返回数字的上入整数

    @x:任意实数类型
    @return:int,x大于等于入参的最小整数
    """

def copysign(x, y):
    """把y的正负号加到x前面

    @x:任意实数类型
    @y:任意实数类型
    @return:float，把 y的正负号加到 x前面
    """

def cos(x):
    """返回x的弧度的余弦值

    @x:任意实数类型
    @return:float，x的弧度的余弦值，范围-1~1之间
    """

def degrees(x):
    """将弧度转换为角度

    @x:任意实数类型
    @return:float，弧度 x转换为角度
    """

e: float = ...  # 数学常量e，e即自然常数。

def exp(x):
    """返回e的x次幂

    @x:任意实数类型
    @return:float，e的 x次幂
    """

def fabs(x):
    """返回数字的绝对值

    @x:任意实数类型
    @return:float，x的绝对值
    """

def floor(x):
    """返回数字的下舍整数

    @x:任意实数类型
    @return:int，x:小于等于入参的最大整数
    """

def fmod(x, y):
    """返回x/y的余数

    @x:任意实数类型
    @y:任意实数类型
    @return:float,x/y的余数
    """

def modf(x):
    """返回由x的小数部分和整数部分组成的元组。

    @x:任意实数类型
    @return:float,x/y的余数
    """

def frexp(x):
    """返回一个元组(m,e)

    @x:浮点数
    @return:tuple,例：(m,e)
    以 (m,e)对的形式返回x的尾数和指数。m是一个浮点数，e是一个整数，正好是x==m*2**e。如果x为零，则返回(0.0,0)，否则返回0.5<=abs(m)<1
    """

def isfinite(x):
    """判断x是否为有限数

    @x:任意实数类型
    @return:bool,判断x是否为有限数，是则返回True，否则返回False。
    """

def isinf(x):
    """判断是否无穷大或负无穷大
    @x:任意实数类型
    @return:如果x是正无穷大或负无穷大，则返回True,否则返回False。
    """

def isnan(x):
    """判断是否非数字（NaN）

    @x:任意实数类型
    @return:如果x为非数字，返回True,否则返回False。
    """

def ldexp(x, exp):
    """返回x*(2^i)的值
    @x:任意实数类型
    @return:float，返回x(2*i)的值。
    """

def log(x):
    """返回x的自然对数

    @x:任意实数类型，小于0会报错
    @return:float，返回x的自然对数
    """

pi: float = ...  # 数学常量pi（圆周率，一般以π来表示）。

def radians(x):
    """将角度转换为弧度
    @x:任意实数类型
    @return:float，将角度x转换为弧度
    """

def sin(x):
    """返回x弧度的正弦值

    @x:任意实数
    @return:float，返回x弧度的正弦值，数值在-1到1之间。
    """

def sqrt(x):
    """返回x的平方根

    @x:任意实数类型
    @return:float，返回数字x的平方根
    """

def tan(x):
    """返回x弧度的正切值

    @x:任意实数类型
    @return:float，返回x弧度的正切值，数值在-1到1之间。
    """

def trunc(x):
    """返回x的整数部分

    @x:任意实数类型
    @return:int，返回x的整数部分。
    """
