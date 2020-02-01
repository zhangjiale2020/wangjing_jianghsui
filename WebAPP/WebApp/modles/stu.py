#!/usr/bin/env python
# encoding: utf-8

"""
@Time   : {2019/12/13} {0:31}
@Author : jooden
@Desc   :
"""
from WebAPP.WebApp.ext import db


class Stu(db.Model):
    __tablename__ = 'stu'
    id = db.Column(db.Integer, primary_key=True, doc='id')
    username = db.Column(db.String, nullable=False, doc='用户名')
    math = db.Column(db.Integer, nullable=False, doc='数学')
    english = db.Column(db.Integer, nullable=False, doc='英语')
    chinese = db.Column(db.Integer, nullable=False, doc='中文')
    zongfen = db.Column(db.Integer, nullable=False, doc='总分')
