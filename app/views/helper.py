#!/usr/bin/env python
# coding: utf-8

from flask import render_template, session, redirect, request
from app.server import OrderServer, FileServer
from app import app

@app.route('/helper/now', methods=['GET'])
@app.route('/helper')
def now():
    orderlist = OrderServer.getHelperOrder()
    if not orderlist or len(orderlist) == 0 or orderlist[0]['status'] == -1:
        return render_template('/helper/now_post.html',phone=session['id'])
    else:
        #data = OrderServer.getOrderNum(orderlist[0]['campus'])
        #number = data[0] + data[1]
        filelist = orderlist[0]['yunfile']
        return render_template('/helper/now_exist.html', order=orderlist[0], filelist=filelist)
            
@app.route('/helper/order/add', methods=['POST'])
def addorder():
    name = protect(request.form['name'])
    bbs = protect(request.form['bbs'])
    local = protect(request.form['local'])
    model = protect(request.form['model'])
    os = protect(request.form['os'])
    desc = protect(request.form['desc'])
    OrderServer.addOrder(bbs, local, model, os, desc, name)
    return redirect("/helper/now")

@app.route('/helper/upload', methods=['POST'])
def yunfile_upload():
    oid = request.form['oid']
    name = protect(request.form['name'])
    ext = protect(request.form['ext'])
    ext = ext.upper()
    if oid and name and ext:
        FileServer.addFile(name, oid, ext)
        return '{"success":true}'
    else:
        return '{"success":false}'

@app.route('/helper/history', methods=['GET'])
def history():
    orderlist = OrderServer.getHelperOrder()
    return render_template('/helper/history.html', orderlist=orderlist)
    
@app.route('/helper/reply', methods=['POST'])
def helperReply():
    referer = request.environ['HTTP_REFERER']
    order = request.form['order']
    content = protect(request.form['content'])
    OrderServer.helperReply(order, content)
    return redirect(referer)

@app.route('/helper/order/del/<oid>', methods=['GET'])
def delorder(oid):
    OrderServer.delOrder(oid)
    return redirect("/helper/now")
    
@app.route('/helper/modify', methods=['GET','POST'])
def modifyorder():
    if request.method == 'POST':
        name = protect(request.form['name'])
        oid = request.form['oid']
        bbs = protect(request.form['bbs'])
        local = protect(request.form['local'])
        model = protect(request.form['model'])
        os = protect(request.form['os'])
        desc = protect(request.form['desc'])
        OrderServer.modifyOrder(oid, bbs, local, model, os, desc, name)
        return redirect("/helper/now")
       
    else:
        orderlist = OrderServer.getHelperOrder()
        print orderlist
        if not orderlist or len(orderlist) == 0 or orderlist[0]['status'] == -1:
            return redirect("/helper/now")
        else:
            for each in orderlist[0]['comments']:
                if each['username'] == session['account']: 
                    each['username'] = "我";
            return render_template('/helper/modify.html', order=orderlist[0])

def protect(word):
    word = word.replace('&','&amp;')
    word = word.replace('<','&lt;')
    word = word.replace('>','&gt;')
    word = word.replace(' ','&nbsp;')
    word = word.replace('\n','<br />')
    word = word.replace('"','&quot;')
    return word