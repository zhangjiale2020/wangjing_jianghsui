#!/usr/bin/env python
# encoding: utf-8

"""
@Time   : {2019/12/20} {17:14}
@Author : jooden
@Desc   :
"""
from WebAPP.WebApp.ext import db
from sqlalchemy import text
import datetime


class ShopPriceModel(db.Model):
    __tablename__ = 't_shop_price'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, default=0, doc='价格')
    shop_id = db.Column(db.Integer, default=0, doc='与店铺表id连接')
    number = db.Column(db.Integer, default=1, doc='用餐人数')
    status = db.Column(db.SmallInteger, default=1, doc='状态：1默认，0删除')
    create_time = db.Column(db.TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), doc='创建时间')
    update_time = db.Column(db.TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
                            doc='更新时间')
