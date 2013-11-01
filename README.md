wormhole
========

RPC base on zmq.
tomdb

Installation
=====

requires: **libzmq,pyzmq**  
依赖模块libzmq,pyzmq
``$ pip install pyzmq``
项目安装:
``$ python setup install

Getting Started
=====
SERVER
```python
from wormhole.server import Server
server = Server(10001)
server.test = lambda x:x*5
server.run()
```

CLIENT
```python
from wormhole.client import Client
client = Client("127.0.0.1", 10001)
test_result,err = client.test("hello!")
if not err:
    print test_result
else:
    print err
```

**更多例子见example.**