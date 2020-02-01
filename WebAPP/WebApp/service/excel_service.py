#!/usr/bin/env python
# encoding: utf-8

"""
@Time   : {2019/12/12} {17:36}
@Author : jooden
@Desc   :
"""
import arrow
from flask import Flask, request
from ksher import BaseService
from WebAPP.WebApp.ext import db
from WebAPP.WebApp.modles import Jiangshui
from WebAPP.WebApp.utils.utils import ExcelUtil


class ExcelService(BaseService):
    """
    向表中添加数据：
    """

    def read_txt(self, ):
        # if request.methods == 'GET':
        data_url = r"D:\wangjing\jiangshui_\2010\SURF_CLI_CHN_MUL_DAY-PRE-13011-201012.TXT"
        # data_list = []
        # if not data_url:
        #     return self.render_error3(-1, '没有数据')
        with open(data_url, "r") as f:  # 设置文件对象,with 是异常处理的
            data = f.readlines()
            current_list = []  # 这是暂时储存地方
            current_month = 0
            point = ''
            for r in data:
                r = r.strip()  # 去除开头和结尾的空格
                r = r.split(' ')  # 以空格分隔元素
                r = [int(i) for i in r if i != '']  # 去除空格 并且保留成int型
                current_list.append(r)  # 将r中的数据暂存在current——list中
                if r[7] in [32700, 32766, 32744, 999990] or r[8] in [32700, 32766, 32744, 999990]:
                    current_list = []
                    current_month = r[5]
                    point = r[0]
                elif point == r[0] and r[5] == current_month:
                    current_list = []
                    continue

                if arrow.get(year=r[4], month=r[5], day=r[6]).format("YYYY-MM-DD") == str(
                        ExcelUtil.get_current_last_day(r[4], r[5])):
                    for e in current_list:
                        if len(str(e[2])) > 4:
                            if int(str(e[2])[:3]) >= 180:
                                e[2] = float(str(e[2])[:2] + str((1 / 60 * int(str(e[2])[-3:])))[1:5])
                            else:
                                e[2] = float(str(e[2])[:3] + str((1 / 60 * int(str(e[2])[-2:])))[1:5])
                        elif len(str(e[2])) > 3:
                            if int(str(e[2])[:3]) >= 180:
                                e[2] = float(str(e[2])[:2] + str((1 / 60 * int(str(e[2])[-2:])))[1:5])
                            else:
                                e[2] = float(str(e[2])[:3] + str((1 / 60 * int(str(e[2])[-1:])))[1:5])
                        elif len(str(e[2])) == 3:
                            if int(str(e[2])[:3]) >= 180:
                                e[2] = float(str(e[2])[:2])
                            else:
                                e[2] = float(str(e[2])[:2] + str((1 / 60 * int(str(e[2])[-1:])))[1:5])
                        new_dict = {'site': e[0],
                                    'latit': float(str(e[1])[:2] + str((1 / 60 * int(str(e[1])[-2:])))[1:5]),
                                    'longit': e[2],
                                    'altit': e[3],
                                    'year': e[4],
                                    'month': e[5],
                                    'day': e[6],
                                    'water_1': e[7],
                                    'water_2': e[8],
                                    'water_sum': e[9],
                                    'freshwater_1': e[10],
                                    'freshwater_2': e[11],
                                    'freshwater_sum': e[12]
                                    }
                        new_item = Jiangshui(**new_dict)
                        db.session.add(new_item)
                    current_list = []
                else:
                    continue
        db.session.commit()
        f.close()
        # print(len(data_list))
        return self.render_success()
