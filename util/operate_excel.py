import xlrd
import xlwt
from xlutils.copy import copy
import sys, os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class OperationExcel:
    def __init__(self, file_path=None, sheet_id=None):
        if file_path:
            self.file_path = file_path
            self.sheet_id = sheet_id
        else:
            self.file_path = PATH('../dataconfig/case1.xls')
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取Excel数据
    def get_data(self):
        data = xlrd.open_workbook(self.file_path)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        """获取行数"""
        tables = self.get_data()
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell(self, row, col):
        return self.data.cell_value(row, col)

    # 写入数据到Excel
    def write_value(self, row, col, value):
        """
        :param row: 行
        :param col:列
        :param value:写入的值
        :return:
        """
        excel = xlrd.open_workbook(self.file_path)
        excel_copy = copy(excel)
        sheet_data = excel_copy.get_sheet(0)
        sheet_data.write(row, col, value)
        excel_copy.save(self.file_path)

    # 获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id is not None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols

    # 根据应对的caseid找到对应行的内容
    def get_rows_data(self, case_id):
        row_number = self.get_row_number(case_id)
        rows_data = self.get_row_value(row_number)
        return rows_data

    # 根据应对的caseid找到对应行号
    def get_row_number(self, case_id):
        num = 0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id == col_data:
                return num
            num = num + 1

    # 根据行号找到该行的内容
    def get_row_value(self, row):
        row_data = self.data.row_values(row)
        return row_data


if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_lines())
    print(opers.get_cell(1, 10))
    opers.write_value(2, 12, '123123')
