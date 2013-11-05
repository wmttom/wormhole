#coding:utf-8
from wormhole.client import Client

client = Client("127.0.0.1", 9528)

time_zone = 0
time_now,err1 = client.get_time(time_zone)
if not err1:
    print "{0} timezone time_now:{1}\n".format(time_zone, time_now)

info = "lsdjflsdajlfjs.jflsajfl"
md5_info,err2 = client.get_md5(info)
if not err2:
    print "{0}\nMD5:{1}\n".format(info, md5_info)

all_sum,err3 = client.get_num(12,2131,12231,123,532,123,123,123,453,7,65)
if not err3:
    print "all_sum: {0}".format(all_sum)