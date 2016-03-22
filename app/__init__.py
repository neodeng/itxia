#!/usr/bin/env python
# coding: utf-8

from flask import Flask
from mongokit import Connection
from app import config

app = Flask(__name__)
app.config.from_object(config)

db = Connection(app.config['MONGODB_HOST'], app.config['MONGODB_PORT'])

from app.views import user, helper, knight