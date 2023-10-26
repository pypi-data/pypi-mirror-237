#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import xlwings

def encrypt_excel(old_filename, new_filename, password):
    '''加密表格'''
    app = xlwings.App(visible=False, add_book=False)
    workbook = app.books.open(old_filename)
    workbook.api.Password = password
    workbook.save(new_filename)
    workbook.close()
    app.quit()