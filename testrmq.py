from rmq import *
from time import sleep

class Test(Rmq):
    def callback(self, ch, method, props, body):
        print body


t = Test()
t.publish('test', 'test')
t.publish('test', 'test')
t.publish('test', 'test')
t.publish('test', 'test')
t.start_recieving('test')
