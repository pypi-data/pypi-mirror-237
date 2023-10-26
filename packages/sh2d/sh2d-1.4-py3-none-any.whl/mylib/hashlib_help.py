#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import hashlib
import secrets

def md5(msg, encoding='utf8'):
    ''''
    计算文本或文件的md5
    :target : 文本或文件路径
    :encoding : 文本编码
    '''
    if os.path.exists(msg):
        md5_hash = hashlib.md5()
        with open(msg, "rb") as f:
            for m in iter(lambda: f.read(4096), b""):
                md5_hash.update(m)
        return md5_hash.hexdigest()
    else:
        return hashlib.md5(msg.encode(encoding)).hexdigest()

def sha1(msg, encoding='utf8'):
    ''''
    获取字符串sha1
    :param _str: 字符串
    '''
    return hashlib.sha1(msg.encode(encoding)).hexdigest()

def sha256(_str, encoding='utf8'):
    ''''
    获取字符串sha256
    :param _str: 字符串
    '''
    return hashlib.sha256(_str.encode(encoding)).hexdigest()
    
    
def gen_md5():
    random_string = secrets.token_hex(16)
    return hashlib.md5(random_string.encode('utf8')).hexdigest()

