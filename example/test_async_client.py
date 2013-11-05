#coding:utf-8
from wormhole.client import AsyncClient

client = AsyncClient("127.0.0.1", 9527)

time_zone = 0
client.get_time(time_zone)
print 1
info = "dlljlfjsaldjfldsjfldsjoifdsijfoidjofdsojfosdajfosdjfosdojfjodsjofajoijoiijsoadfjo"
client.get_md5(info)
print 2
client.get_num(12,2131,12231,123,532,123,123,123,453,7,65)
print 3