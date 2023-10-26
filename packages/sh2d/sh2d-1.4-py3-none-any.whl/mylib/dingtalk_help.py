#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import hmac
import hashlib
import base64
import urllib.parse
import requests
import logging

logger = logging.getLogger("main.dingtalk")


def _sign(secret):
    timestamp = str(round(time.time() * 1000))
    hmac_code = hmac.new(secret.encode('utf-8'), '{}\n{}'.format(timestamp,
                         secret).encode('utf-8'), digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return timestamp, sign


def send_text(text, webhook, secret="", atMobiles=[], isAtAll=False):
    """
    发送消息到钉钉群
    :param text: 发送的文本消息
    :param webhook: 钉钉群机器人webhook
    :param secret: 钉钉群机器人secret,为关键字或IP限制时可为空
    :param atMobiles: 要at的人的手机号列表
    :param isAtAll: 是否@全部人 默认False
    """
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {
            "atMobiles": atMobiles,
            "isAtAll": isAtAll},
    }
    if secret:
        timestamp, sign = _sign(secret)
        url = f"{webhook}&timestamp={timestamp}&sign={sign}"
    try:
        rj = requests.post(url, json=data, headers=headers).json()
        if rj['errcode'] == 0:
            logger.debug(f'send {text[:20]} {rj["errmsg"]}')
            return True
        else:
            logger.warning(f'send {text[:20]} {rj["errmsg"]}')
            return False
    except:
        logger.error(f'send {text[:20]} 失败')
        return False


def send_markdown(title, text, webhook, secret="", atMobiles=[], isAtAll=False):
    """
    发送消息到钉钉群
    :param title: 发送的markdown标题
    :param text: 发送的markdown内容
    :param webhook: 钉钉群机器人webhook
    :param secret: 钉钉群机器人secret,为关键字或IP限制时可为空
    :param atMobiles: 要at的人的手机号列表
    :param isAtAll: 是否@全部人 默认False
    """
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": text
        },
        "at": {
            "atMobiles": atMobiles,
            "isAtAll": isAtAll},
    }
    if secret:
        timestamp, sign = _sign(secret)
        url = f"{webhook}&timestamp={timestamp}&sign={sign}"
    try:
        rj = requests.post(url, json=data, headers=headers).json()
        if rj['errcode'] == 0:
            logger.debug(f'send {title} {rj["errmsg"]}')
            return True
        else:
            logger.warning(f'send {title} {rj["errmsg"]}')
            return False
    except:
        logger.error(f'send {title} 失败')
        return False