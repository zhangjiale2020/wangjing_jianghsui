#!/usr/bin/env python
# encoding: utf-8

"""
@Time   : {2019/12/19} {10:06}
@Author : jooden
@Desc   :
"""

from ksher import BaseService
from WebAPP.WebApp.ext import db
from WebAPP.WebApp.modles import ShopInfoModel, ShopCategoryModel, ShopPriceModel
from flask import request, Flask
import pandas as pd


def Upload_Shop(**params):
    # """
    # 向shop_info中添加数据：
    # :return:
    # """
    # # 1.导入数据
    # # a = request.files['upload']
    # a = 'C://Users//EDZ//Desktop//Bespo_20200120.csv'
    # data = pd.read_csv(a,  header=None, encoding='gbk', skiprows='',
    #                    names=['shop_id', 'shop_name', 'shop_image', 'long', 'lat',
    #                           'cate1', 'cate2', 'address', 'price', 'images',
    #                           'phone', 'des', 'extra', 'tag']).fillna('None')
    # # 2.转化类型为dict型
    # data_list = data.to_dict(orient='records')
    # cate_dict = {}
    # shop_price = {}
    # # 3.遍历数据，拿到所要字段
    # for r in data_list:
    #     shop_dict = {'shop_id': r.get('shop_id'),
    #                  'shop_name': {'cn': str(r.get('shop_name')), 'en': '', 'jp': str(r.get('shop_name'))},
    #                  'shop_image': {'HeadImage': {'data': [[r.get('shop_image')], [r.get('images')]], 'home': 1}},
    #                  'longitude': r.get("long"),
    #                  'latitude': r.get("lat"),
    #                  'address': {'cn': r.get('address'), 'en': '', 'jp': ''},
    #                  'mobile': [r.get('phone')],
    #                  'remarks': r.get('des'),
    #                  'extra': {'cn': r.get('extra'), 'en': '', 'jp': ''},
    #                  'order_check_to_shop': r.get('tag'),
    #                  }
    #     # 3.1 向cate_dict[]添加数据  list(cate_dict.keys()) ==[1,2,3,4],[list(cate_dict.values()).index(r.get('cate1'))] =[0]
    #     if r.get('cate1') in cate_dict.values():
    #         cate_id = list(cate_dict.keys())[list(cate_dict.values()).index(r.get('cate1'))]
    #     # elif r.get('price') in shop_price.values():
    #     #     _shop_id = list(shop_price.keys())[list(shop_price.values()).index(r.get('price'))]
    #     # 3.2 判断是是否是空值，是的话返回0(空)
    #     elif r.get('cate1') != 'None':
    #         # 给ShopCategoryModel 给添加数据
    #         new_cate_info = ShopCategoryModel(**{'category_name': r.get('cate1'), 'saas_app_id': 2096})
    #         db.session.add(new_cate_info)
    #         db.session.flush()
    #         cate_id = new_cate_info.category_id
    #         cate_dict[str(cate_id)] = r.get('cate1')
    #     else:
    #         cate_id = 0
    #     # 4.导入数据库数据
    #     shop_dict['category_id'] = cate_id
    #     ShopInfoModel.insert_data(shop_dict)
    # db.session.commit()
    # return 'ok'
    pass

