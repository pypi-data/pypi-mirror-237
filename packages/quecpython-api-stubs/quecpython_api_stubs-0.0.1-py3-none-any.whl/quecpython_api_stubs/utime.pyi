"""
Function:
utime模块用于获取当前时间、测量时间间隔和休眠。该模块实现相应CPython模块的子集。更多信息请参阅CPython文档：https://docs.python.org/3.5/library/time.html#module-time

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/utime.html
"""


def localtime(secs=None):
    """提供seconds参数时将一个以秒为单位的时间转换为一个日期格式的时间并返回；不提供seconds参数时返回本地RTC的时间。

    @secs:int类型，一个以秒为单位的时间。
    @return:类型为元组，(year, month, day, hour, minute, second, weekday, yearday)，包含了年、月、日、时、分、秒、星期、一年中第几天。当提供参数secs时，返回转换后的时间。当参数secs没有提供时，则返回本地RTC的时间。返回值含义如下：
    元组成员	范围及类型	含义
    year	int型	年份
    month	int型，1~12	月份
    day	int型，1~31	日，当月多少号
    hour	int型，0~23	小时
    minute	int型，0~59	分钟
    second	int型，0~59	秒
    weekday	int型，周一到周日是0~6	星期
    yearday	int型	一年中的第多少天
    """

def mktime(date):
    """将一个存放在元组中的日期格式的时间转换为以秒为单位的时间并返回。
    @date:日期格式的时间，类型为元组，格式：(year, month, mday, hour, minute, second, weekday, yearday)。
    @return: 时间戳(seconds)
    """

def time():
    """返回自设备开机以来的秒数。"""

def getTimeZone():
    """获取当前时区(int类型，单位小时，范围[-12, 12]，负值表示西时区，正值表示东时区，0表示零时区。)。"""

def setTimeZone(offset):
    """设置时区。设置时区后，本地时间会随之变化为对应时区的时间。

    @offset:int类型，单位小时，范围[-12, 12]，负值表示西时区，正值表示东时区，0表示零时区。
    @return:成功返回0，失败抛异常。
    """

def getTimeZoneEx():
    """获取当前时区（增强型），精度更高，可获取非整数时区。
    增强型时区读取/设置接口须成对使用，如使用原有的时区接口读取非整数时区，会造成精度丢失。当前仅EC200A系列支持该功能。

    @return:float类型，单位小时，范围[-12.0, 12.0]，负值表示西时区，正值表示东时区，0.0表示零时区。
    """

def setTimeZoneEx(offset):
    """设置时区（增强型），精度更高，可设置非整数时区。设置时区后，本地时间会随之变化为对应时区的时间。
    增强型时区读取/设置接口须成对使用，如使用原有的时区接口读取非整数时区，会造成精度丢失。当前仅EC200A系列支持该功能。

    @offset:float类型，单位小时，范围[-12.0, 12.0]，最大精度为0.25小时（即参数须为0.25的整数倍）负值表示西时区，正值表示东时区，0.0表示零时区。
    return:成功返回0，失败抛异常。
    """

def ticks_ms():
    """返回不断递增的毫秒计数器，在超过0x3FFFFFFF值后会重新计数。

    @return:int类型，毫秒计数值，计数值本身无特定意义，只适合用在ticks_diff()函数中。
    """

def ticks_us():
    """返回不断递增的微秒计数器，在超过0x3FFFFFFF值后会重新计数。

    @return:int类型，微秒计数值，计数值本身无特定意义，只适合用在ticks_diff()函数中。
    """

def ticks_cpu():
    """返回不断递增的cpu计数器，单位不确定，取决于硬件平台底层的时钟。

    @return:int类型，计数值，计数值本身无特定意义，只适合用在ticks_diff()函数中。
    """

def ticks_diff(ticks1, ticks2):
    """计算两次调用ticks_ms，ticks_us，或ticks_cpu之间的时间间隔。因为ticks_xxx这些函数的计数值可能会回绕，所以不能直接相减，需要使用ticks_diff函数。通常用法是在带超时的轮询事件中调用。
    ticks2和ticks1的顺序不能颠倒，否则结果无法确定。且这个函数不要用在计算很长的时间间隔，具体限制为ticks2和ticks1的tick差值不能超过0x1FFFFFFF，否则结果无法确定。

    @ticks1-int类型，第二次调用ticks_ms，ticks_us，或ticks_cpu获取的tick值。
    @ticks2-int类型，第一次调用ticks_ms，ticks_us，或ticks_cpu获取的tick值。
    @return:int类型，时间间隔，两次调用ticks_ms，ticks_us，或ticks_cpu之间的时间间隔。单位和传入的ticks2和ticks1的单位一致。
    """

def sleep(seconds):
    """休眠给定秒数的时间。函数的调用会导致程序休眠阻塞。

    @seconds:类型，休眠的时长，单位秒。
    """

def sleep_ms(ms):
    """休眠给定毫秒数的时间。函数的调用会导致程序休眠阻塞。

    @ms:int类型，休眠的时长，单位毫秒。
    """

def sleep_us(us):
    """休眠给定微秒数的时间。函数的调用会导致程序休眠阻塞。

    @us:int类型，休眠的时长，单位微秒。
    """
