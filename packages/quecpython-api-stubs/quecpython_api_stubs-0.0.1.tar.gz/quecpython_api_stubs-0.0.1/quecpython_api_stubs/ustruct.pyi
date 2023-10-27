"""
Function:
ustruct模块实现相应CPython模块的子集。更多信息请参阅CPython文档：https://docs.python.org/3.5/library/struct.html#module-struct

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/ustruct.html

格式字符串
格式字符串是用来在打包和解包数据时指定预期布局的机制。其使用指定被打包/解包数据类型的格式字符进行构建。 此外，还有一些特殊字符用来控制字节顺序，大小和对齐方式。

字节顺序，大小和对齐方式
默认情况下，C类型以机器的本机格式和字节顺序表示，并在必要时通过跳过填充字节来正确对齐（根据C编译器使用的规则）。根据下表，格式字符串的第一个字符可用于指示打包数据的字节顺序，大小和对齐方式：

+---------------+---------------+-----------+-------------------------------+
|   Character   |   Byte order  |           |       Size    |   Alignment   |
+===============+===============+===========+===============+===============+
|       @       |   native                  |   native      |   native      |
|       =       |   native                  |   standard    |   none        |
|       <       |   little-endian           |   standard    |   none        |
|       >       |   big-endian              |   standard    |   none        |
|       !       |   network (= big-endian)  |   standard    |   none        |
+---------------+---------------------------+---------------+---------------+
如果第一个字符不是其中之一，则假定为 '@' 。

格式化字符表
+-----------+-------------------+---------------+-------------------+
|   Format  |   C Type          |   Python type |   Standard size   |
+===========+===================+===============+===================+
|   b       |   signed char     |   integer     |       1           |
|   B       |   unsigned char   |   integer     |       1           |
|   h       |   short           |   integer     |       2           |
|   H       |   unsigned short  |   integer     |       2           |
|   i       |   int             |   integer     |       4           |
|   I       |   unsigned int    |   integer     |       4           |
|   l       |   long            |   integer     |       4           |
|   L       |   unsigned long   |   integer     |       4           |
|   q       |   long long       |   integer     |       8           |
|   Q       |   unsigned long   |   long        |       8           |
|   f       |   float           |   float       |       4           |
|   d       |   double          |   float       |       8           |
|   P       |   void *          |   integer     |       4           |
+-----------+-------------------+---------------+-------------------+
"""


def calcsize(fmt):
    """计算并返回存放fmt需要的字节数。

    @fmt:格式字符的类型，详情见上文格化式字符表
    @返回存放fmt需要的字节数。
    """

def pack(fmt, *args):
    """按照格式字符串fmt压缩参数...

    @fmt:格式字符的类型，详情见上文格化式字符表
    @args:是需要进行数据转换的变量名或值
    @return:返回参数编码后的字节对象。
    """

def unpack(fmt, data):
    """根据格式化字符串fmt对数据进行解压，返回值为一个元组。

    @fmt:格式字符的类型，详情见上文格化式字符表
    @data:要进行解压的数据
    @return:返回包含解压值的元组(即使只包含一个项)。
    """

def pack_into(fmt, buffer, offset, *args):
    """根据格式字符串fmt将值args打包到从offset开始的缓冲区中。从缓冲区的末尾算起，offset可能为负。

    @fmt:格式字符的类型，详情见上文格化式字符表
    @buffer:可写数据缓冲区
    @offset:写入的起始位置
    @args:需要写入缓冲区的数据
    """

def unpack_from(fmt, data, offset=0):
    """根据格式化字符串fmt解析从offset开始的数据解压，从缓冲区末尾开始计数的偏移量可能为负值。

    @fmt:格式字符的类型，详情见上文格化式字符表
    @data:数据缓冲区(缓冲区大小以字节为单位)
    @offset:(可选)解压的起始位置，默认为零
    @return:返回解压值的元组(即使只包含一个项)。
    """
