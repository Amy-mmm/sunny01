"""
 利用httpserver程序，编写一个fork多进程程序
，让用户既可以通过8000端口访问端应用也可以通过8080
端口访问后端应用。
"""
import os
from httpserver import *

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    main(('0.0.0.0',8000))
else:
    main(('0.0.0.0', 8080))


