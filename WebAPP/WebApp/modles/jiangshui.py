#!/usr/bin/env python
# encoding: utf-8

"""
@Time   : {2019/12/12} {10:04}
@Author : jooden
@Desc   :
"""
from WebAPP.WebApp.ext import db


class Jiangshui(db.Model):
    __tablename__ = 'jiangshui'  # 下滑波浪线是因为单词错误，但是这种写法是必须这样写的。
    id = db.Column(db.Integer, primary_key=True, doc='ID')
    site = db.Column(db.Integer, nullable=False, doc='站点')
    latit = db.Column(db.Integer, nullable=False, doc='纬度')
    longit = db.Column(db.Integer, nullable=False, doc='经度')
    altit = db.Column(db.Integer, nullable=False, doc='高度')
    year = db.Column(db.Integer, nullable=False, doc='年')
    month = db.Column(db.Integer, nullable=False, doc='月')
    day = db.Column(db.Integer, nullable=False, doc='日')
    water_1 = db.Column(db.Integer, nullable=False, doc='20-8降水')
    water_2 = db.Column(db.Integer, nullable=False, doc='8-20降水')
    water_sum = db.Column(db.Integer, nullable=False, doc='8-20降水总量')
    freshwater_1 = db.Column(db.Integer, nullable=False, doc='20-8降水量质量控制码')
    freshwater_2 = db.Column(db.Integer, nullable=False, doc='8-20累计降水量质量控制码')
    freshwater_sum = db.Column(db.Integer, nullable=False, doc='20-20时水量质量控制码')