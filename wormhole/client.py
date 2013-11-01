#coding:utf-8
import zmq
import json

context = zmq.Context()

class Client(object):

    def __init__(self, ip, port):
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