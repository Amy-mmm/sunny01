"""
编写一个服务端http程序，在客户端发起request请求时
将网页按照http响应格式发送给浏览器展示

温馨提示： 网页的内容是响应体,注意协调响应格式

         对请求做一定的解析判断，如果请求内容是
         / 则发送这个网页
         如果是其他的则 用 404 进行响应
"""

from socket import *

# 处理具体请求
def handle(connfd):
    # http请求
    request = connfd.recv(4096).decode()
    if not request:
        return
    # 从http请求中提取请求内容
    request_line = request.split('\n')[0]
    info = request_line.split(' ')[1]

    # 根据请求内容组织响应
    if info == '/':
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += '\r\n'
        with open('index.html') as f:
            response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += '\r\n'
        response += 'Sorry.....'
    # 将响应发送给浏览器
    connfd.send(response.encode())

# 搭建tcp网络
def main(addr):
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(addr)
    sockfd.listen(3)
    while True:
        try:
            # 等浏览器链接
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            break
        handle(connfd) # 处理浏览器请求

    sockfd.close()

if __name__ == '__main__':
    main(('0.0.0.0',8000))






