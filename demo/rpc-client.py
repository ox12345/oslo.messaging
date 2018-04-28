import os
from sys import argv
from oslo.config import cfg
from oslo import messaging
import logging
logging.basicConfig(filename=os.path.join(os.getcwd(), 'publish_log.txt'),
                    level=logging.WARN,
                    filemode='w',
                    format='%(asctime)s - %(levelname)s: %(message)s')

CONF = cfg.CONF
CONF(args=argv[1:])

# transport means how to conncet rabbitmq-server
transport = messaging.get_transport(CONF)

# target cover the queue, exchange, server, for example
# rcp.server is a queue name
target = messaging.Target(topic='rpc', server='server')

# genenate rpc-client
rpc_client = messaging.RPCClient(transport, target)

# message while sended to rpc-server
kwargs = {"from client":"hello"}

# uncomment code below to send a fanout message which will be sended
# to every node and doesn't wait for response
# cctxt = rpc_client.prepare(fanout=True)
# print cctxt.cast({}, "test", **kwargs)

# uncomment code below to send a cast message which will be sended to
# test.server queue and doesn't wait for response
# print rpc_client.cast({}, "test", **kwargs)

# below call command to send a call message  which will wait for response
print rpc_client.call({}, "test", **kwargs)

