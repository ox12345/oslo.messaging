import os
import eventlet
from sys import argv
from oslo.config import cfg
from oslo import messaging
import logging
logging.basicConfig(filename=os.path.join(os.getcwd(), 'publish_log.txt'),
                    level=logging.WARN,
                    filemode='w',
                    format='%(asctime)s - %(levelname)s: %(message)s')


eventlet.monkey_patch()

# TestEndpoint is a callback class. It consists of endpoints in rpc-server.
# The method in class TestEndpoint is a callback function.
# rpc-client will send method test, and then rpc-server will call
# the callback function to process the request.


class TestEndpoint(object):
    def test(self, ctxt, **kwarg):
        print kwarg
        return {"from server": "hello"}

# read configure file that contains rabbitmq-server's ip\password and so on


CONF = cfg.CONF
CONF(args=argv[1:])

# endpoints means rpc method handler
endpoints = [TestEndpoint(),]

# transport means how to conncet rabbitmq-server
transport = messaging.get_transport(CONF)

# target means how to send messages
target = messaging.Target(topic='rpc',
                          server='server')

# genarator server.
server = messaging.get_rpc_server(transport,
                                  target,
                                  endpoints,
                                  executor='eventlet')
# start rpc-server
server.start()
server.wait()

