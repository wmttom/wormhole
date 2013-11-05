#coding:utf-8
import zmq
import json
context = zmq.Context()

class Server(object):
    
    def __init__(self, port):
        self.server = context.socket(zmq.REP)
        self.server.bind("tcp://*:{0}".format(port))

    def run(self):
        print "ready"
        while True:
            recv = self.server.recv()
            recv_dict = json.loads(recv)
            func = recv_dict['func']
            arg = recv_dict['arg']
            try:
                if arg:
                    return_main = getattr(self, func)(*arg)
                else:
                    return_main = getattr(self, func)()
            except Exception, ex:
                return_main = None
                return_error = str(ex)
            else:
                return_error = None
            finally:
                self.server.send(json.dumps({"main": return_main, "error":return_error}))


class AsyncServer(object):
    
    def __init__(self, port):
        self.server = context.socket(zmq.PULL)
        self.server.bind("tcp://*:{0}".format(port))

    def run(self):
        print "ready"
        while True:
            recv = self.server.recv()
            recv_dict = json.loads(recv)
            func = recv_dict['func']
            arg = recv_dict['arg']
            try:
                if arg:
                    return_main = getattr(self, func)(*arg)
                else:
                    return_main = getattr(self, func)()
            except Exception, ex:
                print ex