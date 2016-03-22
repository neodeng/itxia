#!/usr/bin/env python
# coding: utf-8

from flask import session
from app import db
from app.models import Member

def checkInfo():
    if 'status' and 'location' and 'account' in session:
        return session['status']
    else:
        session.clear()
        return "wrong"
        
def login(account, pw):
    userInfo = db.itxia_database.members.one({'account':account})
    if userInfo:
        if (userInfo['password'] == pw):
            if (userInfo['authority'] == 1):
                result = "admin"
            else:
                result = "knight"
            session['id'] = str(userInfo['_id'])
            session['status'] = result
            session['account'] = account
            session['location'] = userInfo['campus']
        else:
            result = u"密码错误"
    else:
        if account.isdigit() and len(account) < 20:
            if (account == pw):
                result = "helper"
                session['id'] = account
                session['status'] = result
                session['location'] = "donothave"
                session['account'] = account
            else:
                result = u"两次电话不相同"
        else:
            result = u"请输入正确的电话号码"
    return result

def logout():
    session.clear()
    pass

def getLocation():
    return session['location']
    pass
    
def allknight():
    result = []
    try:
        userInfo = db.itxia_database.members.find()
        for each in userInfo:
            result.append(each)
    except Exception, e:
        print e
    return result
    
def addknight(name, account, pw, location):
    try:
        newkn = db.itxia_database.members.Member()
        newkn['name'] = name
        newkn['account'] = account
        newkn['password'] = pw
        newkn['campus'] = location
        newkn.save()
        return 1
    except:
        return None

def upadmin(account):
    try:
        ac = db.itxia_database.members.Member.one({'account':account})
        ac['authority'] = 1
        ac.save()
        return 1
    except:
        return None

def delknight(account):
    try:
        db.itxia_database.members.remove({'account':account})
        return 1
    except:
        return None
        
        