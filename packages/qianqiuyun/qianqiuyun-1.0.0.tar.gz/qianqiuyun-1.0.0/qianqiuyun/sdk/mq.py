import nats

def get_mq():
    nc = nats.connect('nats://nats-server:4222')
    return nc