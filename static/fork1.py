"""
fork1.py  fork演示2
"""
import os
from time import sleep

print("=========================")
a = 1

# 创建子进程
pid = os.fork()
if pid < 0:
    print('Create process failed')
elif pid == 0:
    # 子进程执行部分
    print("Child process")
    print("a = ",a) # 从父进程拷贝了内存a的值
    a = 10000 # 只修改自己空间的a
else:
    sleep(1)
    # 父进程执行部分
    print("Parent process")
    print("a:",a)

print("All a=",a) # 父子进程都执行




