from WebAPP.WebApp.ext import db


class LangModel(db.Model):
    __tablename__ = 'ksher_katakana'
    id = db.Column(db.Integer, primary_key=True)
    pinyin = db.Column(db.String, doc='拼音')
    katakana = db.Column(db.String, doc='日语片假名')
