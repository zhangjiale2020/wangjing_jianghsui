# -*- coding:utf-8 -*-
from WebAPP.WebApp.ext import db
from WebAPP.WebApp.modles import LangModel
from ksher import BaseService
import pandas as pd
from pypinyin import lazy_pinyin

import sys
import codecs
import time

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


# import os
# import sys
# import importlib
# importlib.reload(sys)
# os.environ['NLS_LANG'] = 'Simplified Chinese_CHINA.ZHS16GBK'

class GetLong(BaseService):

    def get_lang(cls, **params):
        """
        jpLang表的上传
        :return:
        """
        filepath = r"C:\Users\EDZ\Desktop\lang.csv"
        data = pd.read_csv(filepath, header=0, encoding='gbk', names=['pinyin', 'jia_ming']).fillna('None')
        _data = data.to_dict(orient='records')

        for pin in _data:
            new_jplang = LangModel()
            new_jplang.pinyin = pin.get('pinyin')
            new_jplang.katakana = pin.get('jia_ming')
            db.session.add(new_jplang)
        db.session.commit()
        # return render_success().set_data('ok')
        return 'ok'

    def jia_ming(self):
        xing = "张"
        ming = '嘉乐'
        xing_ming = xing + ming
        pinyin = lazy_pinyin(xing_ming)
        jia_ming = ""
        for item in pinyin:
            query = db.session.query(LangModel.pinyin, LangModel.katakana).filter(LangModel.pinyin == item).first()
            katakana = query.katakana
            jia_ming += katakana.decode('utf-8')
        return self.render_success().set_data({'jia_ming': jia_ming, 'xing': xing, 'ming': ming}).get_json()

    def query_name_and_katakana(self):
        db_query = db.session.query(LangModel.pinyin, LangModel.katakana).all()
        for item in db_query:
            pinyin = item.pinyin.decode('utf-8')
            katakana = item.katakana.decode('utf-8')
            result = '"' + pinyin + '"' + ' ' + ' : ''"' + katakana + '"' + ','
            # print(pinyin + '', ':', katakana)
            print(result)

        return 'ok'
