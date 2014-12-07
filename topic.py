from rmq import *
from time import sleep

class Topic(Rmq):
    def callback(self, ch, method, props, body):
        print ch
        print method
        print props
        print body

t = Topic()
t.exchange_declare('topic', 'supertopic')
t.queue_bind('some-queue', 'supertopic', 'topic.is.awesome.#')
t.publish('topic.is.awesome.dude.you.know?', 'test', 'supertopic')
t.start_recieving('some-queue')
