from flask import Flask, render_template, send_file
from WebAPP.WebApp.ext import db
from WebAPP.WebApp.service import emptyblist, excel_service, write_excle,  Upload_Shop, Cha_Ru, GetLong

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:zjl961102@127.0.0.1:3306/mydb1?charset=utf8mb4'
# app.config[
#     'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://zhengxiaowen:Qaz123@112.74.105.10:3306/ksher_mch?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)  # 初始化连接数据库，防止连接泄露，保护好数据


@app.route('/')
def hello_world():
    return render_template('read_txt.html')


@app.route('/r/', methods=['GET', 'POST'])
def read_txt():
    """
    存储功能
    :param params:
    :return:
    """
    # data_url = request.files['upload']
    return excel_service.read_txt()


@app.route('/w/')
def write_excel():
    """
    下载功能
    """
    return send_file(write_excle.write_excel(), as_attachment=True, attachment_filename="降水数据.xlsx")


@app.route('/q/')
def delete_data():
    """
    删除功能的实现:清空数据库中数据
    :return:
    """
    return emptyblist.delete_data()


# @app.route('/d/', methods=['POST'])
def upload_shop(**params):
    """
    向shop_info中添加数据：
    """
    return Upload_Shop().upload_shop()


@app.route('/wread/')
def cha_du(**params):
    """
    第二种：存入.csv的方法
    """
    # return Cha_Ru().Cha_ru()
    return Cha_Ru().get_site()


@app.route('/get_long')
def get_long(**params):
    # return GetLong().get_lang()
    return GetLong().jia_ming()
    # return GetLong().query_name_and_katakana()


if __name__ == '__main__':
    app.run(debug=True)
