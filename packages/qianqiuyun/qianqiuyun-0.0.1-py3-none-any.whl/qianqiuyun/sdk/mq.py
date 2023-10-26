import nats
import util

def get_mq(ns=None):
    ns = util.get_env_ns(ns)
    nc = nats.connect('nats://nats-server.%s.svc.cluster.local:4222' % ns)
    return nc