#!/usr/bin/env python
# coding: utf-8

from flask import render_template, session, redirect, request
from app.server import UserServer
from app import app

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        name = protect(name)
        password = protect(password)
        if password == 'iamhelper':
            password = name
        result = UserServer.login(name, password)
        if result == "knight" or result == "admin":
            return redirect("/knight/wait")
        elif result == "helper":
            return redirect("/helper/now")
        else:
            return render_template('user/login.html',message = result, username= name, asd=password)
    else:
        check = UserServer.checkInfo()
        if check == "knight" or check == "admin":
            return redirect("/knight/wait")
        elif check == "helper":
            return redirect("/helper/now")
        return render_template('user/login.html')

@app.route('/knightlogin', methods=['GET'])
def knightlogin():
    check = UserServer.checkInfo()
    if ((check == "knight") or (check == "admin")):
        return redirect("/knight/wait")
    elif (check == "helper"):
        return redirect("/helper/now")
    return render_template('user/knightlogin.html')

@app.route('/logout', methods=['GET'])
def logout():
    UserServer.logout()
    return redirect('/')

    
def protect(word):
    word = word.replace('&','&amp;')
    word = word.replace('<','&lt;')
    word = word.replace('>','&gt;')
    word = word.replace(' ','&nbsp;')
    word = word.replace('\n','<br />')
    word = word.replace('"','&quot;')
    return word