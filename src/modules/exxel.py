"""
Name: Omnivision
Author: Dakota Carter
License: MIT
Description: This module is for fucking writing to an excel.
"""

import xlwt
from xlwt import Workbook
from datetime import datetime

def write_excel(links, images, forms):
    werkberk = Workbook(encoding='utf-8')
    key_style = xlwt.easyxf("font: bold on;")
    cell_style = xlwt.easyxf("align: wrap on, horiz left, vert center;")
    sheets = [links, images, forms]
    for sheet in sheets:
        current_sheet = werkberk.add_sheet(str(sheet.category))
        # Write these keys
        current_sheet.write(0, 0, 'Name', style=key_style)
        current_sheet.write(0, 1, 'Attributes', style=key_style)
        current_sheet.write(0, 2, 'From', style=key_style)
        current_sheet.write(0, 3, 'Link', style=key_style)
        current_sheet.write(0, 4, 'Status', style=key_style)
        current_sheet.write(0, 5, 'Message', style=key_style)
        if sheet.category == 'images':
            current_sheet.write(0, 6, 'Data', style=key_style)
            current_sheet.write(0, 7, 'Data-Valid', style=key_style)
        for index, element in enumerate(sheet):
            current_sheet.write(index+1, 0, element.name, style=cell_style)
            current_sheet.write(index+1, 1, str(element.attrs), style=cell_style)
            current_sheet.write(index+1, 2, element.url, style=cell_style)
            current_sheet.write(index+1, 3, element.check, style=cell_style)
            current_sheet.write(index+1, 4, element.status, style=cell_style)
            current_sheet.write(index+1, 5, element.message, style=cell_style)
            if sheet.category == 'images':
                current_sheet.write(index+1, 6, element.validate, style=cell_style)
                current_sheet.write(index+1, 7, element.is_valid, style=cell_style)
    werkberk.save('Omnivision-{}.xls'.format(datetime.now().strftime('%Y-%m-%d__%H_%M_%S')))