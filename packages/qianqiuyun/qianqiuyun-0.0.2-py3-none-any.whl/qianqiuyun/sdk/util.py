import os

def get_env_ns(ns=None):
    if ns is None:
        ns = os.getenv('ENV_QIANQIUYUN_NAMESPACE')
        if ns is None:
            ns='qianqiuyun'
    return ns