"""
Function:
该模块提供对BSD套接字接口的访问。该模块实现相应CPython模块的子集。更多信息请参阅阅CPython文档：https://docs.python.org/3.5/library/socket.html#module-socket

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/usocket.html
"""


AF_INET = ...  # 地址族，IPV4类型。
AF_INET6 = ...  # 地址族，IPV6类型。
SOCK_STREAM = ...  # socket类型，TCP的流式套接字。
SOCK_DGRAM = ...  # socket类型，UDP的数据包套接字。
SOCK_RAW = ...  # socket类型，原始套接字。
IPPROTO_TCP = ...  # 协议号，TCP协议。
IPPROTO_UDP = ...  # 协议号，UDP协议。
IPPROTO_TCP_SER = ...  # 协议号，TCP服务器。
TCP_CUSTOMIZE_PORT = ...  # 协议号，TCP客户端自定义address使用。
SOL_SOCKET = ...  # 套接字选项级别。
SO_REUSEADDR = ...  # socket功能选项，允许设置端口复用。
TCP_KEEPALIVE = ...  # socket功能选项，设置TCP保活包间隔时间。


class socket(object):

    def __init__(self, af=AF_INET, type=SOCK_STREAM, proto=IPPROTO_TCP):
        """根据给定的地址族、套接字类型以及协议类型参数，创建一个新的套接字对象。注意，在大多数情况下不需要指定proto，也不建议这样做，因为某些MicroPython端口可能会省略IPPROTO_*常量。

        @af:地址族（参考常量说明）。
        @type:socket类型（参考常量说明）。
        @proto:协议号（参考常量说明）。
        """

    def getaddrinfo(self, host, port):
        """DNS域名解析，将主机域名（host）和端口（port）解析为用于创建套接字的5元组序列。

        @host:主机域名。
        @port:端口。
        @return: tuple，(family, type, proto, canonname, sockaddr);
        family,地址族（参考常量说明）;
        type,socket类型（参考常量说明）;
        proto,协议号（参考常量说明）;
        canonname,主机域名;
        sockaddr,包含地址和端口号的列表。
        """

    def bind(self, address):
        """该方法用于套接字绑定指定address，必须尚未绑定。
        1、作为服务器时，需要进行绑定，以固定服务器的address。
        2、作为客户端时，绑定address用来指定套接字进行数据处理（配合usocket.TCP_CUSTOMIZE_PORT使用）。

        @address:包含地址和端口号的元组或列表。
        """

    def listen(self, backlog):
        """该方法用于套接字服务端开启监听客户端连接，可指定最大客户端连接数。

        @backlog:接受套接字的最大个数，至少为0。
        """

    def accept(self):
        """该方法用于套接字服务端接受连接请求。

        @return:成功返回元组，包含新的套接字和客户端地址以及客户端端口，形式为：(conn,address,port)。
        conn,新的套接字对象，用来和客户端交互;
        address,连接到服务器的客户端地址;
        port,连接到服务器的客户端端口。
        """

    def connect(self, address):
        """该方法用于套接字连接到指定address的服务器。

        @address:包含地址和端口号的元组或列表。
        """

    def read(self, size=None):
        """该方法用于从套接字中读取数据。

        @size:int,读取size字节数据。如果没有指定size，则会从套接字读取所有可读数据，直到读取到数据结束，此时作用和socket.readall()相同。
        @return:返回一个字节对象。
        """

    def readinto(self, buf, nbytes=None):
        """该方法用于从套接字读取字节到缓冲区buf中。如果指定了nbytes，则最多读取nbytes数量的字节；如果没有指定nbytes，则最多读取len(buf)字节。

        @buf:字节缓冲区buf。bytearray
        @nbytes:int,读取nbytes数量的字节
        @return:返回值是实际读取的字节数。
        """

    def readline(self):
        """该方法用于从套接字按行读取数据，遇到换行符结束，返回读取的数据行。"""

    def write(self, buf):
        """该方法用于套接字发送缓冲区的数据。

        @buf:待发送的字节数据。
        @return:返回实际发送的字节数
        """

    def send(self, buf):
        """该方法用于套接字发送缓冲区的数据。

        @buf:待发送的字节数据。
        @return:返回实际发送的字节数
        """

    def sendall(self, buf):
        """该方法用于套接字将所有数据都发送到套接字。与send()方法不同的是，此方法将尝试通过依次逐块发送数据来发送所有数据。该方法再非阻塞套接字上的行为是不确定的，建议在MicroPython中，使用write()方法，该方法具有相同的“禁止短写”策略来阻塞套接字，并且将返回在非阻塞套接字上发送的字节数。

        @buf:待发送的字节数据。
        """

    def sendto(self, buf, address):
        """该方法用于套接字发送数据到指定address。

        @buf:待发送缓的字节数据。
        @address:包含地址和端口号的元组或列表。
        @return:返回实际发送的字节数。
        """

    def recv(self, size):
        """该方法用于从套接字接收数据。返回值是一个字节对象，表示接收到的数据。一次接收的最大数据量由size指定。

        @size:一次接收的最大数据量。
        """

    def recvfrom(self, size):
        """该方法用于从套接字接收数据。返回一个元组，包含字节对象和地址。

        @size:一次接收的最大数据量。
        @return:返回值形式为：(bytes, address)。bytes，接收数据的字节对象；address，发送数据的套接字的地址。
        """

    def close(self):
        """该方法用于将套接字标记为关闭并释放所有资源。"""

    def setsockopt(self, level, optname, value):
        """该方法用于设置套接字选项的值。

        @level:套接字选项级别。
        @optname:socket功能选项。
        @value:既可以是一个整数，也可以是一个表示缓冲区的bytes类对象。
        """

    def setblocking(self, flag):
        """该方法用于设置套接字为阻塞模式或者非阻塞模式。该方法是settimeout()调用的简写。

        @flag:设置套接字是否阻塞（默认为阻塞模式）。
        """

    def settimeout(self, timeout):
        """该方法用于设置套接字的发送和接收数据超时时间，单位秒。

        @timeout:超时时间，单位秒。
        """

    def makefile(self, mode='rb'):
        """该方法用于返回与套接字关联的文件对象，返回值类型与指定的参数有关。仅支持二进制模式(rb和wb)。

        @mode:打开文件的模式，"rb"或者"wb"。
        @return:返回与套接字关联的文件对象。
        """

    def getsocketsta(self):
        """该方法用于获取TCP套接字的状态。BG95平台不支持该API。如果调用了socket.close()方法之后，再调用 socket.getsocketsta()会返回-1，因为此时创建的对象资源等都已经被释放。

        @return:返回socket状态值。如下：
        状态值	状态	描述
        0	CLOSED	套接字创建了，但没有使用这个套接字
        1	LISTEN	套接字正在监听连接
        2	SYN_SENT	套接字正在试图主动建立连接，即发送SYN后还没有收到ACK
        3	SYN_RCVD	套接字正在处于连接的初始同步状态，即收到对方的SYN，但还没收到自己发过去的SYN的ACK
        4	ESTABLISHED	套接字已成功建立连接
        5	FIN_WAIT_1	套接字已关闭，正在关闭连接，即发送FIN，没有收到ACK也没有收到FIN
        6	FIN_WAIT_2	套接字已关闭，正在等待远程套接字关闭，即在FIN_WAIT_1状态下收到发过去FIN对应的ACK
        7	CLOSE_WAIT	远程套接字已经关闭，正在等待关闭这个套接字，被动关闭的一方收到FIN
        8	CLOSING	套接字已关闭，远程套接字正在关闭，暂时挂起关闭确认，即在FIN_WAIT_1状态下收到被动方的FIN
        9	LAST_ACK	远程套接字已关闭，正在等待本地套接字的关闭确认，被动方在CLOSE_WAIT状态下发送FIN
        10	TIME_WAIT	套接字已经关闭，正在等待远程套接字的关闭，即FIN、ACK、FIN、ACK都完毕，经过2MSL时间后变为CLOSED状态
        """
