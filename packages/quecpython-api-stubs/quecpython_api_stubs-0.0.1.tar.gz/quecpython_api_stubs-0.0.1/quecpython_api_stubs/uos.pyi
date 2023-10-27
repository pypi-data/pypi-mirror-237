"""
Function:
uos模块包含文件系统访问和挂载构建，该模块实现了CPython模块相应模块的子集。更多信息请参阅CPython文档：https://docs.python.org/3.5/library/os.html#module-os

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/uos.html
"""
from typing import Callable


def remove(path: str) -> None:
    """删除文件。

    @path:字符串，表示文件名。
    """

def chdir(path) -> None:
    """改变当前目录。

    @path:字符串，表示目录名。
    """

def getcwd() -> str:
    """获取当前路径。

    @return:字符串，当前路径。
    """

def listdir(dir: str = '/') -> tuple:
    """列出当前目录文件。

    @dir:字符串，指定目录路径。
    @return:元组，列出路径下所有存在的对象，如["file1", "file2" ...]
    """

def mkdir(path: str) -> None:
    """创建一个新的目录。

    @path:备创建的目录名，为所在目录的相对路径。
    """

def rename(old_path: str, new_path: str) -> None:
    """重命名文件。

    @old_path:字符串，表示旧文件或目录名，
    @new_path:字符串，表示新文件或目录名。
    """

def rmdir(path) -> None:
    """删除指定目录。

    @path:字符串，表示目录名，为所在目录的相对路径。
    """

def ilistdir(dir: str = '') -> tuple:
    """该函数返回一个迭代器，该迭代器会生成所列出条目对应的3元组。

    @dir:为可选参数，字符串，表示目录名，没有参数时，默认列出当前目录，有参数时，则列出dir参数指定的目录。
    @return:返回一个迭代器，该迭代器会生成所列出条目对应的3元组。
    元组的形式为(name, type, inode[, size])
    name是条目的名称，字符串类型，如果dir是字节对象，则名称为字节;
    type是条目的类型，整型数，0x4000表示目录，0x8000表示常规文件；
    inode是一个与文件的索引节点相对应的整数，对于没有这种概念的文件系统来说，可能为0；
    一些平台可能会返回一个4元组，其中包含条目的size。对于文件条目，size表示文件大小的整数，如果未知，则为-1。对于目录项，其含义目前尚未定义。
    """

def stat(path) -> tuple:
    """获取文件或目录的状态。

    @path:字符串，表示文件或目录名。
    @return:返回值是一个元组，返回值形式为(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
    mode – inode保护模式
    ino – inode节点号
    dev – inode驻留的设备
    nlink – inode的链接数
    uid – 所有者的用户ID
    gid – 所有者的组ID
    size – 文件大小，单位字节
    atime – 上次访问的时间
    mtime – 最后一次修改的时间
    ctime – 操作系统报告的“ctime”，在某些系统上是最新的元数据更改的时间，在其它系统上是创建时间，详细信息参见平台文档
    """

def statvfs(path: str) -> tuple:
    """获取文件系统状态信息。

    @path:字符串，表示文件或目录名。
    @return:返回一个包含文件系统信息的元组(f_bsize, f_frsize, f_blocks, f_bfree, f_bavail, f_files, f_ffree, f_favail, f_flag, f_namemax)
    f_bsize – 文件系统块大小，单位字节
    f_frsize – 分栈大小，单位字节
    f_blocks – 文件系统数据块总数
    f_bfree – 可用块数
    f_bavai – 非超级用户可获取的块数
    f_files – 文件结点总数
    f_ffree – 可用文件结点数
    f_favail – 超级用户的可用文件结点数
    f_flag – 挂载标记
    f_namemax – 最大文件长度，单位字节
    """

def uname() -> tuple:
    """获取关于底层信息或其操作系统的信息。

    @return:该接口与micropython官方接口返回值形式有所区别，返回一个元组，形式为(sysname, nodename, release, version, machine)
    sysname – 底层系统的名称，string类型
    nodename – 网络名称(可以与 sysname 相同) ，string类型
    release – 底层系统的版本，string类型
    version – MicroPython版本和构建日期，string类型
    machine – 底层硬件(如主板、CPU)的标识符，string类型
    qpyver – QuecPython 短版本号，string类型
    """

def uname2() -> tuple:
    """获取关于底层信息或其操作系统的信息。

    @return:该接口与micropython官方接口返回值形式一致。注意与上面uos.uname()接口返回值的区别，返回值形式为(sysname, nodename, release, version, machine, qpyver)
    sysname – 底层系统的名称，string类型
    nodename – 网络名称(可以与 sysname 相同) ，string类型
    release – 底层系统的版本，string类型
    version – MicroPython版本和构建日期，string类型
    machine – 底层硬件(如主板、CPU)的标识符，string类型
    qpyver – QuecPython 短版本号，string类型
    """

def urandom(n: int) -> bytes:
    """返回具有n个随机字节的bytes对象，如果模组搭载了硬件随机数生成器，它就会由硬件随机数生成器生成。

    @n:整型，随机字节的个数
    @return:具有n个随机字节的bytes对象
    """

def VfsFat(spi_port: int, spimode: int, spiclk, spics):
    """初始化SD卡，和SD卡通信。使用SPI通信方式。

    @spi_port:通道选择[0,1]
    @spimode:SPI的工作模式(模式0最常用)
    参数  工作模式
    0	CPOL=0,CPHA=0
    1	CPOL=0,CPHA=1
    2	CPOL=1,CPHA=0
    3	CPOL=1,CPHA=1
    时钟极性CPOL:即SPI空闲时，时钟信号SCLK的电平（0:空闲时低电平; 1:空闲时高电平）
    @spiclk:时钟频率枚举值
    参数  时钟频率
    0   812.5kHz
    1   1.625MHz
    2   3.25MHz
    3   6.5MHz
    4   13MHz
    @spics:int，指定CS片选引脚为任意GPIO，硬件CS可以接这里指定的脚，也可以接默认的CS脚
    1-n:指定Pin.GPIO1-Pin.GPIOn为CS脚
    @return:成功则返回VfsFat对象，失败则会抛出异常。
    """

def VfsSd(s: str = 'sf_fs'):
    """初始化SD卡，使用SDIO通信方式。

    @s:固定为"sd_fs"，后续扩展。
    @return:成功则返回vfs object，失败则会报错。
    """

def set_det(GPIOn: int, mode: int) -> int:
    """int类型，用于sd卡插拔卡检测的GPIO引脚号，参照Pin模块的定义

    @GPIOn:用于sd卡插拔卡检测的GPIO引脚号，参照Pin模块的定义。
    @mode:0,sd卡插上后，检测口为低电平；sd卡取出后，检测口为高电平;1,sd卡插上后，检测口为高电平；sd卡取出后，检测口为低电平。
    @return:成功返回 0，失败返回 -1。
    """

def set_callback(fun: Callable) -> int:
    """设定发生插拔卡事件时的用户回调函数。目前仅EC600U/EC200U平台支持。

    @fun:插拔卡的回调函数，function类型，原型为fun(args),参数args为int类型，0表示拔卡，1表示插卡
    @return:成功返回 0，失败返回 -1。
    """

def VfsLfs1(readsize: int, progsize: int, lookahead: int, pname: str, spi_port: int, spi_clk: int):
    """初始化spi nor flash,和外挂nor flash通信。使用SPI通信方式,将此存储设备挂载为littleFS文件系统。目前仅ECx00N&EGx00N&ECx00M&EGx00M&ECx00U&EGx00U系列平台支持

    @readsize:预留，暂未使用
    @progsize:预留，暂未使用
    @lookahead:预留，暂未使用
    @pname:固定为“ext_fs”。后续扩展
    @spi_port:支持的端口参照SPI章节说明
    @spi_clk:时钟频率
    参数	时钟频率
    0	6.25MHz
    1	12.5MHz
    2	25MHz
    3	50MHz
    4	3.125MHz
    5	1.5625MHz
    6	781.25KHz
    @return:成功则返回VfsLfs1 object,失败则返回OSError19。
    """

def VfsEmmc(s: str):
    """初始化EMMC存储，使用SDIO通信方式。目前仅EC200ACNLA平台支持

    @str:预留，暂未使用。
    @return:成功则返回vfs对象，失败则会报错。
    """

def mount(vfs_obj, path: str, mkfs: int):
    """挂载实体文件系统(如littleFS/FATFS等)到虚拟文件系统(VFS)。

    @vfs_obj，vfs object，文件系统对象
    @path，str类型，文件系统的根目录
    @mkfs，int类型，可选参数，是否格式化存储设备。传入1执行格式化，不传入该参数或传入0不执行格式化。格式化功能适用于SD卡存储及EC600MCN_CC_EXT&ECx00U&EGx00U系列平台外置SPI NOR flash存储场景。
    """
