#!/usr/bin/env python
# coding: utf-8

from app.models import Member
from app import db

admin = db.itxia_database.members.Member()
admin['account'] = 'itxia'
admin['password'] = 'itxia'
admin['campus'] = '鼓楼'
admin['authority'] = 1
admin.save()