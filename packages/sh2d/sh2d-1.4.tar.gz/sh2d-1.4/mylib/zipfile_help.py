#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import datetime
import zipfile


def unzip(zip_file, unzip_dir):
    """
    解压zip文件到指定目录 
    :param zip_file  zip文件
    :param unzip_dir 解压目录
    """
    f = zipfile.ZipFile(zip_file, 'r')
    for file in f.namelist():
        f.extract(file, unzip_dir)


def make_zip_v1(source_dir, output_filename):
    """
    打包文件夹（不包含根目录）
    :param source_dir  要打包的目录
    :param output_filename 打包后的文件名
    """
    zip = zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED)
    for path, _, filenames in os.walk(source_dir):
        fpath = path.replace(source_dir, '')
        for filename in filenames:
            zip.write(os.path.join(path, filename),
                      os.path.join(fpath, filename))
    zip.close()


def make_zip_v2(source_dir, output_filename):
    """
    打包文件夹（包含根目录）
    :param source_dir  要打包的目录
    :param output_filename 打包后的文件名
    """
    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, _, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
            zipf.write(pathfile, arcname)
    zipf.close()


def get_create_time(zip_file_path):
    '''获取压缩包内文件创建时间'''
    result = {}
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        file_list = zip_ref.namelist()
        for file_name in file_list:
            file_info = zip_ref.getinfo(file_name)

            try:
                creation_time = file_info.date_time
                creation_datetime = datetime.datetime(
                    year=creation_time[0],
                    month=creation_time[1],
                    day=creation_time[2],
                    hour=creation_time[3],
                    minute=creation_time[4],
                    second=creation_time[5]
                )
                result[file_name] = creation_datetime
            except KeyError:
                pass
    return result

