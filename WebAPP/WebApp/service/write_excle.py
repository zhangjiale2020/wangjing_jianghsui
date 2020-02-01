#!/usr/bin/env python
# encoding: utf-8

"""
@Time   : {2019/12/12} {18:18}
@Author : jooden
@Desc   :
"""

from ksher.utils.model_util import model_to_dict3
from sqlalchemy import desc
from WebAPP.WebApp.ext import db
from ksher import BaseService
from WebAPP.WebApp.modles import Jiangshui
from WebAPP.WebApp.service import emptyblist
from WebAPP.WebApp.utils.utils import ExcelUtil


class WriteExcle(BaseService):
    """
    下载功能的实现
    """
    def write_excel(self):
        query = db.session.query(Jiangshui).order_by(desc(Jiangshui.latit)).all()
        query_all = [model_to_dict3(e) for e in query]
        req_data = dict()
        req_data['title'] = ['id', 'site', 'latit', 'longit', 'altit', 'year', 'month', 'day', 'water_1', 'water_2',
                             'water_sum', 'freshwater_1', 'freshwater_2', 'freshwater_sum']
        req_data['sheet_name'] = 'JiangShui'
        req_data['content'] = query_all

        # file_stream = ExcelUtil.write_file_stream(**req_data)
        file_stream = ExcelUtil.write_single_simple("C:\\Users\\EDZ\\Downloads\\zjl.xlsx", **req_data)
        # emptyblist.delete_data()
        return file_stream


