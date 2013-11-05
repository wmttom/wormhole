#coding:utf-8
from wormhole.server import Server

server = Server(9528)

def get_time(time_zone):
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.mktime(time.gmtime())+time_zone*3600))

def get_md5(info):
    import hashlib
    return hashlib.md5(info).hexdigest().upper()

def get_num(*arg):
    return sum(arg)

server.get_time = get_time
server.get_md5 = get_md5
server.get_num = get_num
server.run()