#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import configparser


def config2json(path, encoding='utf8'):
    """
    读取配置文件为json
    :param path: 配置文件路径,eg: config.ini/config.conf/config.cfg
    :param encoding: 编码方式
    :return 返回json eg: {"项名":{"选项":"值"}
    """
    _dict = {}
    conf = configparser.RawConfigParser()
    conf.read(path, encoding=encoding)
    sections = conf.sections()
    for item in sections:
        _dict.setdefault(item, {})
        _dict[item].update(dict(conf.items(item)))
    return _dict


def json2config(path, _dict, encoding='utf8'):
    """
    写入json格式配置到文件
    :param path: 配置文件路径,eg: config.ini/config.conf/config.cfg
    :param encoding: 编码方式
    :param _dict: json格式 eg: {"项名":{"选项":"值"}
    """
    conf = configparser.RawConfigParser()
    for section in _dict:
        conf.add_section(section)
        for k, v in _dict[section]:
            conf.set(section, k, v)
    with open(path, 'w', encoding=encoding) as f:
        conf.write(f)
