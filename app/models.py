#!/usr/bin/env python
# coding: utf-8

from app import db
import mongokit
from mongokit import Document
import re

def phone_validator(value):
    phone = re.compile(r'^(13|14|15|17|18)[0-9]{9}$')
    return bool(phone.match(value))

def campus_validator(value):
    campus = ['鼓楼', '仙林']
    if value in campus:
        return True
    else:
        return False

def authority_validator(value):
    authority = [0, 1] # 0:非管理员 1:管理员
    if value in authority:
        return True
    else:
        return False

def status_validator(value):
    status = [-1, 0, 1] # -1:处理完成 0:无人处理 1:正在处理
    if value in authority:
        return True
    else:
        return False

class Member(Document):
    structure = {
        'account': basestring,
        'name': basestring,
        'password': basestring,
        'phone_number': basestring,
        'campus': basestring,
        'authority': int,
        'mail': basestring,
    }
    #validators = {
    #    'phone_number': phone_validator,
    #    'campus': campus_validator,
    #    'authority': authority_validator
    #}
    required_fields = ['account', 'password', 'campus']
    default_values = {'authority': 0,}
    
class Order(Document):
    structure = {
        'phone_number': basestring,
        'name': basestring,
        'lilybbs_id': basestring,
        'campus': basestring,
        'order_time': basestring,
        'machine_model': basestring,
        'operate_system': basestring,
        'description': basestring,
        'status': int,
        'handler': basestring,
        'replybool': int,
        'yunfile':[
            {
                'file_name': basestring,
                'upload_time': basestring,
                'ext': basestring,
            }    
        ],
        'comments': [
            {
                'username': basestring,
                'created_time': basestring,
                'content': basestring,
            }
        ]
    }
    #validators = {
    #    #'phone_number': phone_validator,
    #    'campus': campus_validator,
    #    'status': status_validator
    #}
    required_fields = ['phone_number', 'campus', 'machine_model', 'status', 'description']
    default_values = {'status': 0,}
    
db.register([Member, Order])