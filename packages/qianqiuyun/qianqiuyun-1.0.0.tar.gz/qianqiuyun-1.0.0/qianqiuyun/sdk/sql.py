#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

def get_db():
    db = pymysql.connect(host='mysql', port=3306, user='root', passwd='qianqiu@#20222', db='oadb_cvxa3663')
    return db