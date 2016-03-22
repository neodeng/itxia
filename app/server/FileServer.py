#!/usr/bin/env python
# coding: utf-8

from app.qiniu import rsf
from app.qiniu import rs
from datetime import datetime
from app import db

from app.config import bucketName

def get_qiniu_list():
    rs = qiniu.rsf.Client()
    marker = None
    err = None
    data = []
    while err is None:
        ret, err = rs.list_prefix(
            bucketName, prefix=None, limit=10, marker=marker)
        marker = ret.get('marker', None)
        for item in ret['items']:
            data.append(item['key'])
            pass
    if err is not qiniu.rsf.EOF:
        # 错误处理
        pass
    return data

def get_mysql_list():
    return FileDao.getAllFile()

def getFile(oid):
    return FileDao.getFile(oid)

def delFile(name):
    ret, err = qiniu.rs.Client().delete(bucketName, name)
    FileDao.del_file(name)
    pass

def addFile(name, oid, ext):
    todaydata = datetime.today()
    time = todaydata.strftime('%y-%m-%d %H:%M:%S')
    try:
        order = db.app.orders.one({'_id':oid})
        order['yunfile'].append({'file_name':name, 'upload_time':time, 'ext':ext})
        order.save()
        return 1
    except Exception, e:
        return None
