import influxdb
import util
from influxdb import InfluxDBClient

def get_tsdb(ns=None):
    ns = util.get_env_ns(ns)
    client = InfluxDBClient('influxdb.%s.svc.cluster.local' % ns, 8086, 'qianqiu', 'qian@#20222', 'qianqiuiot')
    return client