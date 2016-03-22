#!/usr/bin/env python
# coding: utf-8

from flask import session
from app import db
from app.models import Order
from datetime import datetime
from mongokit import ObjectId
    
def getHelperOrder():
    orderList = []
    try:
        List = db.itxia_database.orders.find({'phone_number':session['id']}).sort([['_id', -1]])
        for each in List:
            orderList.append(each)
    except Exception, e:
        print e
    return orderList
    
def addOrder(bbs, local, model, os, desc, name):
    todaydata = datetime.today()
    time = todaydata.strftime('%y-%m-%d %H:%M:%S')
    try:
        od = db.itxia_database.orders.Order()
        od['phone_number'] = session['account']
        od['name'] = name
        od['lilybbs_id'] = bbs
        od['campus'] = local
        od['order_time'] = time
        od['machine_model'] = model
        od['operate_system'] = os
        od['description'] = desc
        od['status'] = 0
        od.save()
        return 1
    except Exception, e:
        print e
        return None

def getOrderNum(location):
    num = []
    waitNum = db.itxia_database.orders.find({'campus':location, 'status': 0}).count()
    workNum = db.itxia_database.orders.find({'campus':location, 'status': 1}).count()
    finishNum = db.itxia_database.orders.find({'campus':location, 'status': -1}).count()
    num = [waitNum, workNum, finishNum]
    return num

def getWaitList(location):
    wait = []
    try:
        orderInfo = db.itxia_database.orders.find({'campus':location, 'status':0}).sort([['_id', -1]])
        for each in orderInfo:
            wait.append(each)
    except Exception, e:
        print e
    return wait

def knightReply(oid, content):
    id = session['id']
    oid = str(oid)
    oid = ObjectId(oid)
    todaydata = datetime.today()
    time = todaydata.strftime('%y-%m-%d %H:%M:%S')
    try:
        if (content == ""):
            return 0
        od = db.itxia_database.orders.Order.one({'_id':oid})
        rep = {'username':session['account'],'created_time':time,'content':content}
        if od['comments']:
            od['comments'].append(rep)
        else:
            od['comments'] = [rep,]
        if session['status'] == 'helper':
            od['replybool'] = 1
        else:
            od['replybool'] = 0
        od.save()
        return 1
    except Exception, e:
        print e
        return 0

def helperReply(oid, content):
    knightReply(oid, content)

def getNewReplyOrder(location):
    result = []
    try:
        replyList = db.itxia_database.orders.find({'replybool':1}).sort([['_id',-1]])
        for each in replyList:
            result.append(each)
        return result
    except Exception, e:
        print e
    
def getOrderPhone(oid):
    try:
        od = db.itxia_database.orders.Order.one({'_id':oid})
        return od['phone_number']
    except Exception, e:
        print e
        return None

def delOrder(oid):
    oid = ObjectId(oid)
    if session['account'] == getOrderPhone(oid):
        try:
            db.itxia_database.orders.remove({'_id':oid})
            return 1
        except Exception, e:
            print e
            return None

def modifyOrder(oid, bbs, local, model, os, desc, name):
    try:
        oid = ObjectId(oid)
        od = db.itxia_database.orders.Order.one({'_id':oid})
        od['lilybbs_id'] = bbs
        od['campus'] = local
        od['machine_model'] = model
        od['operate_system'] = os
        od['description'] = desc
        od['name'] = name
        od.save()
        return 1
    except Exception, e:
        print e
        return None

def changeWork(oid):
     try:
         oid = ObjectId(oid)
         od = db.itxia_database.orders.Order.one({'_id':oid})
         od['status'] = 1
         od['handler'] = session['account']
         od.save()
         return 1
     except Exception, e:
        print e
        return None

def getWorkList(location):
    worklist = []
    try:
        orderInfo = db.itxia_database.orders.find({'campus':location, 'status':1}).sort([['_id',-1]])
        for each in orderInfo:
            worklist.append(each)
        return worklist
    except Exception, e:
        print e

def changeWait(oid):
    try:
        oid = ObjectId(oid)
        od = db.itxia_database.orders.Order.one({'_id':oid})
        od['status'] = 0
        od['handler'] = None
        od.save()
        return 1
    except Exception, e:
        print e
        return None
        
def changeFinish(oid):
    try:
        oid = ObjectId(oid)
        od = db.itxia_database.orders.Order.one({'_id':oid})
        od['status'] = -1
        od.save()
        return 1
    except Exception, e:
        print e
        return None

def getFinishList(location, page):
    size = 30
    result = []
    start = page * size
    finish = (page+1) * size
    try:
        orderInfo = db.itxia_database.orders.find({'status':-1}).sort([['_id',-1]])
        for each in orderInfo:
            result.append(each)
        count = len(result)
        if finish > count:
            odpage = result[start:]
        else:
            odpage = result[start:finish]
        return odpage
    except Exception, e:
        print e
        return None
