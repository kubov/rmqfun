from rmq import *
from time import sleep
from threading import Thread

class Gateway(Rmq):
    def callback(self, ch, method, props, body):
        print body


def loop():
    line = None
    rmq = Rmq()
    while line != "exit":
        line = raw_input()
        splits = line.split(" ")
        if len(splits) < 2:
            continue
        key = splits[0]
        message = ' '.join(splits[1:])
        print "[x] sent ", key, message
        rmq.publish(key, message, 'events')
    rmq.connection.close()
    print 'bay'

g = Gateway()
g.exchange_declare('topic', 'events')
t = Thread(target=loop)
t.start()

try:
    g.start_recieving('responses')
except KeyboardInterrupt:
    print "die"
    g.connection.close()
