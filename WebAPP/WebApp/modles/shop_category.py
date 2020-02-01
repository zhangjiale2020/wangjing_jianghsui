#!/usr/bin/env python
# encoding: utf-8

"""
@Time   : {2019/12/19} {18:24}
@Author : jooden
@Desc   :
"""
from WebAPP.WebApp.ext import db
from sqlalchemy import text


class ShopCategoryModel(db.Model):
    __tablename__ = 't_shop_category'
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(32), default='', doc='美食类别名称')
    remark = db.Column(db.String(512), default='')
    saas_app_id = db.Column(db.Integer, default=0, doc='saas_app_id, 0: 全部app, >0 具体')
    status = db.Column(db.SmallInteger, default=1, doc='状态：1默认，0删除')
    create_time = db.Column(db.TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), doc='创建时间')
    update_time = db.Column(db.TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
                            doc='更新时间')
