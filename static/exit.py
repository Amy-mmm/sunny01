"""
exit.py  进程退出
"""
import os,sys

# 父子进程退出互相不会影响对方

# os._exit(0) # 进程退出
sys.exit("退出进程")

print("exit process")