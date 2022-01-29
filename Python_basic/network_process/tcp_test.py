#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import socket

logging.getLogger().setLevel(logging.INFO)


def test():
    """
    create a Socket based on TCP connection
    Socket是网络编程的一个抽象概念。
    通常我们用一个Socket表示“打开了一个网络链接”，
    而打开一个Socket需要知道目标计算机的IP地址和端口号，
    再指定协议类型即可。

    Client:
    大多数连接都是可靠的TCP连接。创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。

    :return:
    """

    # create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    """
    创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。
    SOCK_STREAM指定使用面向流的TCP协议，
    这样，一个Socket对象就创建成功，但是还没有建立连接。"""

    #  create connection
    s.connect(('www.sina.com.cn', 80))
    """
    客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号。
    新浪网站的IP地址可以用域名www.sina.com.cn自动转换到IP地址，但是怎么知道新浪服务器的端口号呢？
    答案是作为服务器，提供什么样的服务，端口号就必须固定下来。
    由于我们想要访问网页，因此新浪提供网页服务的服务器必须把端口号固定在80端口，因为80端口是Web服务的标准端口。
    其他服务都有对应的标准端口号，
    例如SMTP服务是25端口，
    FTP服务是21端口，等等。
    端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。
    """

    # send data
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    """
    TCP连接创建的是双向通道，双方都可以同时给对方发数据。
    但是谁先发谁后发，怎么协调，要根据具体的协议来决定。
    例如，HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。
    """

    # receive data
    buffer = []
    while True:
        # each time receive 1k Bytes most
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    """
    接收数据时，调用recv(max)方法，一次最多接收指定的字节数，
    因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。
    """

    s.close()

    """
    接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，
    把HTTP头打印出来，网页内容保存到文件：
    """
    header, html = data.split(b'\r\n\r\n', 1)
    logging.info(f'header encoding: {header.decode("utf-8")}')

    # write recive data into file
    with open('sina.html', 'wb') as f:
        f.write(html)


if __name__ == '__main__':

    test()
    """
    INFO:root:header encoding: HTTP/1.1 302 Moved Temporarily
    Server: nginx
    Date: Sat, 29 Jan 2022 08:23:18 GMT
    Content-Type: text/html
    Content-Length: 138
    Connection: close
    Location: https://www.sina.com.cn/
    X-Via-CDN: f=edge,s=cnc.beixian.union.219.nb.sinaedge.com,c=202.108.14.240;
    
    Process finished with exit code 0

    """