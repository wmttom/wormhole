#coding:utf-8
import zmq
import json

context = zmq.Context()

class Client(object):

    def __init__(self, ip, port, green=False):
        if green == True:
            import zmq.green as zmq
        self.client = context.socket(zmq.REQ)
        self.client.connect("tcp://{0}:{1}".format(ip,port))
    
    def __getattr__(self, attr):
        def _(*arg):
            return self.send(attr, *arg)
        return _

    def send(self, func, *arg):
        send_dict = {'func':func,'arg':arg}
        self.client.send(json.dumps(send_dict))
        recv = self.client.recv()
        recv_dict = json.loads(recv)
        return recv_dict['main'], recv_dict['error']


class AsyncClient(object):

    def __init__(self, ip, port, green=False):
        if green == True:
            import zmq.green as zmq
        else:
            import zmq
        self.client = context.socket(zmq.PUSH)
        self.client.connect("tcp://{0}:{1}".format(ip,port))
    
    def __getattr__(self, attr):
        def _(*arg):
            return self.send(attr, *arg)
        return _

    def send(self, func, *arg):
        send_dict = {'func':func,'arg':arg}
        self.client.send(json.dumps(send_dict))

class TornadoClient(object):

    def __init__(self, ip, port):
        from zmq.eventloop.zmqstream import ZMQStream
        self.client = context.socket(zmq.REQ)
        self.client.connect("tcp://{0}:{1}".format(ip,port))
        self.stream = ZMQStream(self.client)
    
    def __getattr__(self, attr):
        def _(*arg):
            return self.send(attr, *arg)
        return _

    def send(self, func, callback, *arg, **kwargs):
        send_dict = {'func':func,'arg':arg}
        self.callback = callback
        self.stream.send(json.dumps(send_dict))
        self.stream.on_recv(self._recv_msg, True)

    def _recv_msg(self, msg):
        recv_dict = json.loads(msg[0])
        main = recv_dict['main']
        err = recv_dict['error']
        self.callback(main, err)


class TornadoAsyncClient(object):

    def __init__(self, ip, port):
        from zmq.eventloop.zmqstream import ZMQStream
        self.client = context.socket(zmq.PUSH)
        self.client.connect("tcp://{0}:{1}".format(ip,port))
        self.stream = ZMQStream(self.client)
    
    def __getattr__(self, attr):
        def _(*arg):
            return self.send(attr, *arg)
        return _

    def send(self, func, *arg):
        send_dict = {'func':func,'arg':arg}
        self.stream.send(json.dumps(send_dict))

def tornado_loop():
    from zmq.eventloop import ioloop
    ioloop.install()