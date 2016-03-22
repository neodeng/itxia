#!/usr/bin/env python
# coding: utf-8

from flask import render_template, session, redirect, request
from app.server import UserServer, OrderServer, FileServer
from app import app

@app.route('/knight/wait', methods=['GET'])
def knightwait():
    status = UserServer.checkInfo()
    location = UserServer.getLocation()
    data = OrderServer.getWaitList(location)
    number = OrderServer.getOrderNum(location)
    user = session['account']
    return render_template('/knight/wait.html', number=number, waitlist=data, status=status, user=user)

@app.route('/knight/setting', methods=['GET'])
def knightset():
    status = UserServer.checkInfo()
    data = UserServer.allknight()
    return render_template('/knight/setting.html',userlist = data, status = status)

@app.route('/knight/setting/add', methods=['POST'])
def addknight():
    try:
        name = protect(request.form['name'])
        account = protect(request.form['account'])
        password = protect(request.form['password'])
        location = protect(request.form['location'])
        UserServer.addknight(name, account, password , location)
        return redirect("/knight/setting")
    except Exception, e:
        print e
        return redirect("/knight/setting")

@app.route('/knight/setting/up/<account>', methods=['GET'])
def upadmin(account):
    account = protect(account)
    UserServer.upadmin(account)
    return redirect("/knight/setting")

@app.route('/knight/setting/del/<account>', methods=['GET'])
def delknight(account):
    account = protect(account)
    UserServer.delknight(account)
    return redirect("/knight/setting")

@app.route('/knight/reply/<time>', methods=['POST'])
def reply(time):
    referer = request.environ['HTTP_REFERER'] + "?p=ihateie"
    try:
        order = request.form['order']
        content = request.form['content']
        OrderServer.knightReply(order, content)
        return redirect(referer)
    except Exception, e:
        print e
        #return redirect(referer)

@app.route('/knight/message', methods=['GET'])
def message():
    status = UserServer.checkInfo()
    location = UserServer.getLocation()
    data = OrderServer.getNewReplyOrder(location)
    number = OrderServer.getOrderNum(location)
    user = session['account']
    return render_template('/knight/message.html',number=number, data=data, status=status, user=user)

@app.route('/knight/towork/<account>', methods=['GET'])
def towork(account):
    oid = account
    if oid:
        OrderServer.changeWork(oid)
    return redirect('/knight/work')

@app.route('/knight/work', methods=['GET'])
def work():
    status = UserServer.checkInfo()
    location = UserServer.getLocation()
    data1 = OrderServer.getWorkList(location)
    number = OrderServer.getOrderNum(location)
    user = session['account']
    data = []
    for each in data1:
        if each['handler'] == user:
            data.append(each)
    for each in data1:
        if not each['handler'] == user:
            data.append(each)
    return render_template('/knight/work.html', number=number, data=data, user=user, status=status)

@app.route('/knight/towait/<account>', methods=['GET'])
def towait(account):
    oid = account
    if oid:
        OrderServer.changeWait(oid)
    referer = request.environ['HTTP_REFERER']
    return redirect(referer)

@app.route('/knight/tofinish/<account>', methods=['GET'])
def tofinish(account):
    oid = account
    if oid:
        OrderServer.changeFinish(oid)
    referer = request.environ['HTTP_REFERER']
    return redirect(referer)

@app.route('/knight/finish/<page>', methods=['GET'])
@app.route('/knight/finish', methods=['GET'])
def finish(page=0):
    status = UserServer.checkInfo()
    page = int(page)
    location = UserServer.getLocation()
    number = OrderServer.getOrderNum(location)
    user = session['account']
    data = OrderServer.getFinishList(location, page)
    return render_template('/knight/finish.html',number=number, data=data, page=page, status=status, user=user)

def protect(word):
    word = word.replace('&','&amp;')
    word = word.replace('<','&lt;')
    word = word.replace('>','&gt;')
    word = word.replace('  ','&nbsp;&nbsp;')
    word = word.replace('\n','<br />')
    word = word.replace('"','&quot;')
    return word