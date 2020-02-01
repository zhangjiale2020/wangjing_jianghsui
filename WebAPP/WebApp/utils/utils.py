#!/usr/bin/env python
# encoding: utf-8

"""
@Time   : {2019/12/12} {10:22}
@Author : jooden
@Desc   :
"""
from io import BytesIO

import xlrd
import xlwt
import datetime
import calendar


class ExcelUtil:
    """
    python操作excel
    """

    @classmethod
    def write_single_simple(cls, file_path, **data):
        """
        将数据保存为excel
        :param file_path:
        :param data:
        :return:
        """
        work_book = xlwt.Workbook(encoding='utf-8')
        # 加入工作表
        sheet_name = data.get('sheet_name', 'Sheet1')
        work_sheet = work_book.add_sheet(sheet_name)
        start_row = data.get('row', 0)
        start_col = data.get('col', 0)

        title_list = data.get('title', [])
        title_length = len(title_list)
        write_title = data.get('write_title', 'Y')
        current_row = start_row
        # 写标题
        if write_title == 'Y':
            col_generator = (x for x in range(title_length))
            for e in title_list:
                work_sheet.write(current_row, (start_col + next(col_generator)), e)
            current_row += 1
        # 写内容
        content = data.get('content', [])
        content_length = len(content)
        row_generator = (x for x in range(content_length))
        for e in content:
            col_generator = (x for x in range(title_length))
            row_no = current_row + next(row_generator)
            for title in title_list:
                col_no = next(col_generator)
                work_sheet.write(row_no, start_col + col_no, e.get(title))
        # 保存文件
        work_book.save(file_path)
        return file_path
        # from io import BytesIO
        # sio = BytesIO()
        # work_book.save(sio)  # 这点很重要，传给save函数的不是保存文件名，而是一个StringIO流
        # return self.render_success().set_data(sio.getvalue())

    @classmethod
    def excel_to_dict(cls, path):
        """将excel处理成一个含有多个字典的列表
        参数:
            flie_path: flie_path

        返回值:
            [
                {'work_date':'2018-05-23', 'state':'WORK', 'week_date': '星期一'},
                {'work_date':'2018-05-24', 'state':'REST', 'week_date': '星期二'},
                ...
            ]
        """
        # 获取excel的book对象
        book = xlrd.open_workbook(path)
        # 获取sheet对象
        table = book.sheets()[0]
        nrows = table.nrows
        ncols = table.ncols
        print(nrows, ncols)
        list1 = ((index_x, index_y) for index_x in range(nrows) for index_y in range(ncols) if index_x > 0)
        title_list = table.row_values(0)
        list_res = []
        dict_res = {}
        for tuple_res in list1:
            dict_res = {} if tuple_res[1] == 0 else dict_res
            cell = table.cell(tuple_res[0], tuple_res[1]).value
            dict_res[title_list[tuple_res[1]]] = cell
            list_res.append(dict_res) if tuple_res[1] == len(title_list) - 1 else None
        return list_res

    @classmethod
    def get_current_last_day(self, year=None, month=None):
        """
        获取某一个月的第一天与最后一天
        """
        if year:
            year = int(year)
        else:
            year = datetime.date.today().year
        if month:
            month = int(month)
        else:
            month = datetime.date.today().month
        # 获取当月第一天的星期和当月的总天数
        firstDayWeekDay, monthRange = calendar.monthrange(year, month)
        # 获取当月的第一天
        datetime.timedelta
        last_day = datetime.date(year=year, month=month, day=monthRange)
        return last_day

    @classmethod
    def write_file_stream(cls, file_path, **data):
        """
        将数据保存为excel
        :param file_path:
        :param data:
        :return:
        """
        work_book = xlwt.Workbook(encoding='utf-8')
        # 加入工作表
        sheet_name = data.get('sheet_name', 'Sheet1')
        work_sheet = work_book.add_sheet(sheet_name)
        start_row = data.get('row', 0)
        start_col = data.get('col', 0)

        title_list = data.get('title', [])
        title_length = len(title_list)
        write_title = data.get('write_title', 'Y')
        current_row = start_row
        # 写标题
        if write_title == 'Y':
            col_generator = (x for x in range(title_length))
            for e in title_list:
                work_sheet.write(current_row, (start_col + next(col_generator)), e)
            current_row += 1
        # 写内容
        content = data.get('content', [])
        content_length = len(content)
        row_generator = (x for x in range(content_length))
        for e in content:
            col_generator = (x for x in range(title_length))
            row_no = current_row + next(row_generator)
            for title in title_list:
                col_no = next(col_generator)
                work_sheet.write(row_no, start_col + col_no, e.get(title))
        # 保存文件
        work_book.save(file_path)
        return file_path

