#!/usr/bin/env python
# encoding: utf-8

"""
@Time   : {2019/12/21} {20:35}
@Author : jooden
@Desc   :
"""
import pandas as pd
from ksher import BaseService
from sqlalchemy import or_
import numpy as np
from WebAPP.WebApp.modles import Jiangshui
from flask import request
from WebAPP.WebApp.ext import db


class Cha_Ru(BaseService):
    """
    插入的功能
    """

    def Cha_ru(cls, **params):
        # a = request.files['Upload']
        filepath = r"D:\jiangshui_\1983\SURF_CLI_CHN_MUL_DAY-PRE-13011-198305.TXT"

        data = pd.read_csv(filepath, header=None, nrows=10, sep="\s+", error_bad_lines=False, encoding='utf-8',
                           names=['1', '2', '3', '4', '5',
                                  '6', '7', '8', '9', '10',
                                  '11', '12', '13']).fillna('None')
        print(data)

        data_list = data.to_dict(orient='records')
        dd_list = []
        for e in data_list:
            # r = [int(r) for r in i if r != '']
            # dd_list.append(r)
            # for e in dd_list:

            new_data = {
                'site': e.get('1'),
                'latit': e.get('2'),
                'longit': e.get('3'),
                'altit': e.get('4'),
                'year': e.get('5'),
                'month': e.get('6'),
                'day': e.get('7'),
                'water_1': e.get('8'),
                'water_2': e.get('9'),
                'water_sum': e.get('10'),
                'freshwater_1': e.get('11'),
                'freshwater_2': e.get('12'),
                'freshwater_sum': e.get('13'),
            }
            _list = Jiangshui(**new_data)
            db.session.add(_list)
        db.session.commit()
        return '成功'

    def get_site(self):
        # 0、不需要输入的参数
        # 1、查询出所需字段，
        site_list = []
        water_list = None
        site_list_query = db.session.query(Jiangshui.water_1).all()
        water_list = np.mean(site_list_query)
        # 2、返回所需的site_list

        print(water_list)

        return '0'
