
import json
from sqlalchemy import text
from WebAPP.WebApp.ext import db
from math import radians, cos, sin, asin, sqrt
from ksher.utils.model_util import get_columns


class ShopInfoModel(db.Model):
    __tablename__ = 't_shop_info'
    shop_id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.JSON, doc='店铺名称', info={'cn': '', 'en': '', 'jp': ''})
    shop_image = db.Column(db.JSON, doc='店铺图片', info={"HeadImage": {"data": [], "home": 1}})
    mch_id = db.Column(db.String(8), default="", doc='商户id')
    mall_id = db.Column(db.Integer, default=0, doc='商场')
    country_id = db.Column(db.Integer, default=0, doc='国家')
    city_id = db.Column(db.Integer, default=0, doc='城市')
    longitude = db.Column(db.Numeric, default=0, doc='经度')
    latitude = db.Column(db.Numeric, default=0, doc='纬度')
    address = db.Column(db.JSON, doc='店铺地址', info={'cn': '', 'en': '', 'jp': ''})
    tag = db.Column(db.JSON, doc='门店标签', info=[])
    tag_id = db.Column(db.JSON, doc='标签ID', info=[])
    mobile = db.Column(db.JSON, doc='电话', info=[])
    is_support_chinese = db.Column(db.SmallInteger, default=0, doc='是否支持中文')
    extra = db.Column(db.JSON, doc='扩展信息', info={'cn': '', 'en': '', 'jp': ''})
    status = db.Column(db.SmallInteger, default=1, doc='状态：1显示，0删除,2测试数据,3待审核')
    create_time = db.Column(db.TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    update_time = db.Column(db.TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    # gis = db.Column(Geometry('POINT'), default="ST_GEOMFROMTEXT('POINT(0 0)')", doc="空间位置信息: ST_GEOMFROMTEXT(CONCAT('POINT(',longitude,' ',latitude,')'))")
    remarks = db.Column(db.String(128), default="", doc='备注')
    saas_app_id = db.Column(db.Integer, default=2092, doc='saas_app_id')
    order_check_to_shop = db.Column(db.SmallInteger, default=0, doc='订单结算给商户, 1 是, 0否')
    pay_mch_id = db.Column(db.String(16), default="", doc='支付商户号')
    category_id = db.Column(db.Integer, default=0, doc='店铺分类')

    # 计算两点间距离-m
    @classmethod
    def geodistance(cls, lng1, lat1, lng2, lat2):
        """
        计算距离
        :param lng1:
        :param lat1:
        :param lng2:
        :param lat2:
        :return:
        """
        if lng1 and lat1 and lng2 and lat2:
            lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])
            dlon = lng2 - lng1
            dlat = lat2 - lat1
            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            dis = 2 * asin(sqrt(a)) * 6371 * 1000
            return dis
        return 0

    # 根据距离显示范围
    @classmethod
    def distance_range(cls, distance=0.0):
        '''
        显示距离范围
        :param distance:
        :return:
        '''
        if not distance:
            return ''
        distance = distance if distance else 0.0
        if distance < 1000.0:
            return '{}m'.format(int(distance))
        elif distance < 100000.0:
            return '{}km'.format('%.1f' % float(distance / 1000))
        else:
            return '>100km'

    @classmethod
    def get_shop_info_by_distance(cls, u_longitude, u_latitude, select_columns=None, where_sql='1=1', where_param=None,
                                  order_by=None, distance_where=None, size=0):
        """
        查询店铺信息，带距离
        :param u_longitude:
        :param u_latitude:
        :return:
        """
        if not select_columns:
            columns = get_columns(cls)
            select_columns = ','.join(columns)
        sql = "SELECT {},ST_Distance_Sphere(Point({},{}), gis) as distance FROM {} WHERE {} {} ORDER BY {} {}".format(
            select_columns, u_longitude, u_latitude, cls.__tablename__, where_sql,
            'having {}'.format(distance_where) if distance_where else '', "distance ASC" if not order_by else order_by,
            'limit {}'.format(size) if size else '')
        rs = db.session.execute(text(sql), where_param).fetchall()
        return rs
        # return [dict(r).update({'distance_range': cls.distance_range(r.distance)}) for r in rs]

    @classmethod
    def get_shop_info_by_star(cls, u_longitude, u_latitude, where_sql='1=1', where_param=None, distance_where=None,
                              size=0):
        """
        查询店铺信息，带距离
        :param u_longitude:
        :param u_latitude:
        :return:
        """
        sql = "SELECT A.shop_id as shop_id,A.shop_name as shop_name,A.shop_image as shop_image,A.intro as intro,B.star as star," \
              "A.mall_id as mall_id,CASE WHEN B.star>2 then ST_Distance_Sphere(Point({},{}), A.gis) ELSE  " \
              "ST_Distance_Sphere(Point({},{}), A.gis) + 6371000.0 END as distance," \
              "ST_Distance_Sphere(Point({},{}), A.gis) as star_distance " \
              "FROM t_shop_info A " \
              "LEFT JOIN t_brand_info B on A.brand_id = B.brand_id " \
              "WHERE {} {}" \
              "ORDER BY star_distance ASC {};".format(u_longitude, u_latitude, u_longitude, u_latitude, u_longitude,
                                                      u_latitude,
                                                      where_sql, 'having distance > {}'.format(
                distance_where) if distance_where else '',
                                                      'limit {}'.format(size) if size else '')
        rs = db.session.execute(text(sql), where_param).fetchall()
        return rs

    @classmethod
    def get_shop_info_by_columns(cls):
        """
        查询列
        :return:
        """
        columns = get_columns(cls)
        select_columns = ','.join(columns)
        return select_columns

    @classmethod
    def insert_data(cls, data):
        fields_str = ""
        format_str = ""
        # data['gis'] = "ST_GEOMFROMTEXT('POINT(0 0)')"
        for key, value in data.items():
            fields_str = fields_str + ",`" + key + "`"
            format_str = format_str + "," + ":{}".format(key)
            if isinstance(value, dict) or isinstance(value, list):
                data[key] = json.dumps(value)
        fields_str = fields_str[1:]
        format_str = format_str[1:]
        insert_str = "insert into `{}` ({},gis) values ({},ST_GEOMFROMTEXT('POINT(0 0)'))".format(cls.__tablename__,
                                                                                                  fields_str,
                                                                                                  format_str)
        # print(str(data))
        result = db.session.execute(text(insert_str), data)

        db.session.flush()
        return result.lastrowid

    @classmethod
    def update_data(cls, longitude, latitude, data, where_sql, where_param):
        set_value_str = ""
        # data['gis'] = "ST_GEOMFROMTEXT('POINT(0 0)')"
        for key, value in data.items():
            set_value_str = set_value_str + "," + key + "=:" + key
            if isinstance(value, dict) or isinstance(value, list):
                where_param[key] = json.dumps(value)
            else:
                where_param[key] = value
        set_value_str = set_value_str[1:]
        update_str = "update `{}` set {},gis=ST_GEOMFROMTEXT('POINT({} {})') WHERE {}".format(cls.__tablename__,
                                                                                              set_value_str,
                                                                                              longitude, latitude,
                                                                                              where_sql)
        result = db.session.execute(text(update_str), where_param)
        db.session.flush()
        return result.rowcount
