#!/usr/bin/env python
# coding: utf-8

import os

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

SECRET_KEY = 'adfsa234ds&%%'

basedir = os.path.abspath(os.path.dirname(__file__))

SITE_NAME = u"NJU-IT 侠预约系统"

'''
本地jquery,bootstrap文件
'''
BASEFILE1 = {
   "bs_js":"/static/base/bootstrap.min.js",
   "bs_css":"/static/base/bootstrap.min.css",
   "jq":"/static/base/jquery.min.js"
}

'''
最新jquery,bootstrap文件
'''
BASEFILE2 = {
   "bs_js":"http://cdn.bootcss.com/bootstrap/3.3.0/js/bootstrap.min.js",
   "bs_css":"http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.css",
   "jq":"http://cdn.bootcss.com/jquery/1.11.1/jquery.min.js"
}

'''
make qiniu token to post form
'''
import qiniu.conf
qiniu.conf.ACCESS_KEY = "51ksljf2Ej7CoI5uL5dJWLho-yQQ_XnEptc8_wpv"
qiniu.conf.SECRET_KEY = "EBGm1DhcnSmrpkenVCmmn4JIPfRBLEoZ2JPrmh6j"

import qiniu.rs
bucketName = "lcdisk"
WEBDISKURL = "http://7xiyaj.com1.z0.glb.clouddn.com"
policy = qiniu.rs.PutPolicy(bucketName)
policy.returnUrl = "http://localhost:5000"
qiniu_token = policy.token()

TOKEN = qiniu_token

version = "2.3"
VERSION = version