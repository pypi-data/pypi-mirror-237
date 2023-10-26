#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import win32file
import win32timezone

import win32com.client


def change_file_time(file_path, new_system_time):
    '''修改文件创建时间时间'''
    filehandle = win32file.CreateFile(
        file_path, win32file.GENERIC_WRITE, 0, None, win32file.OPEN_EXISTING, 0, 0)
    win32file.SetFileTime(filehandle, new_system_time,
                          new_system_time, new_system_time)
    filehandle.close()

def encrypt_excel(old_filename,new_filename,new_passwd,old_passwd=''):
    '''设置或修改表格密码'''
    ea = win32com.client.Dispatch("Excel.Application")
    wb = ea.Workbooks.Open(old_filename, False, False, None, old_passwd)
    ea.DisplayAlerts = False
    wb.SaveAs(new_filename, None, new_passwd, '')
    ea.Quit()

def say(text):
    '''文本转系统语音播放'''
    spk = win32com.client.Dispatch("SAPI.SpVoice")
    spk.Speak(text)