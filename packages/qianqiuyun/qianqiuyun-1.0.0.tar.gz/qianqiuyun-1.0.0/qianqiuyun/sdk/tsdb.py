import influxdb

from influxdb import InfluxDBClient

def get_tsdb():
    client = InfluxDBClient('influxdb', 8086, 'qianqiu', 'qian@#20222', 'qianqiuiot')
    return client