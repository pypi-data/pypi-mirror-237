import influxdb
from influxdb import InfluxDBClient
from qianqiuyun.sdk.util import get_env_ns

def get_tsdb(ns=None):
    ns = get_env_ns(ns)
    client = InfluxDBClient('influxdb.%s.svc.cluster.local' % ns, 8086, 'qianqiu', 'qian@#20222', 'qianqiuiot')
    return client