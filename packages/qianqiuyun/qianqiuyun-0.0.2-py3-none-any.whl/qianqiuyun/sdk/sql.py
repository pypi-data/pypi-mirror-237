#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
from qianqiuyun.sdk.util import get_env_ns

def get_db(ns=None):
    ns = get_env_ns(ns)
    db = pymysql.connect(host='mysql.%s.svc.cluster.local' % ns, port=3306, user='root', passwd='qianqiu@#20222', db='oadb_cvxa3663')
    return db