"""
获取http请求
回复相应
"""

from socket import *

# http使用tcp协议
s = socket()
s.bind(('0.0.0.0',8000))
s.listen(3)

c,addr = s.accept() # 链接了浏览器
print("Connect from",addr)
request = c.recv(4096).decode() # 接受请求
print(request)

response="""HTTP/1.1 200 OK
Content-Type:text/html;charset=UTF-8

人生苦短，我用Python。
"""

# response="""HTTP/1.1 404 Not Found
# Content-Type:text/html;charset=UTF-8
#
# Sorry...
# """
c.send(response.encode()) # 发送响应

c.close()
s.close()







