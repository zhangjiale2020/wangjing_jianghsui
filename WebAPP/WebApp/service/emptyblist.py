#!/usr/bin/env python
# encoding: utf-8

"""
@Time   : {2019/12/13} {0:26}
@Author : jooden
@Desc   :
"""
from ksher import BaseService
from WebAPP.WebApp.ext import db
from WebAPP.WebApp.modles import Stu, Jiangshui


class EmptybList(BaseService):
    """
    清空数据表中的数据
    """
    def delete_data(self):
        query = db.session.query(Jiangshui)
        query.delete()
        db.session.commit()
        return '清理成功'
