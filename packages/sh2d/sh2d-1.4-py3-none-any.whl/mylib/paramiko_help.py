#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import paramiko
import logging

logger = logging.getLogger("main.paramiko")

class SSHClient():

    def __init__(self, ip, port, user, passwd):
        """
        初始化函数,创建ssh连接
        :param ip: 传入ip,eg: 127.0.0.1
        :param port: 传入端口 eg: 22
        :param user: 传入用户名 eg: root
        :param passwd: 传入密码 eg: 123456
        """
        self.ip = ip
        self.port = port
        self.user = user
        self.passwd = passwd
        self.transport = None
        self.sftp = None
        self.ssh = None

    def connect(self,mode='ssh'):
        if mode == 'sftp':
            try:
                self.transport = paramiko.Transport((self.ip, int(self.port)))
                self.transport.connect(username=self.user, password=self.passwd)
                self.sftp = paramiko.SFTPClient.from_transport(self.transport)
            except:
                logger.error(f"connect {mode}@{self.ip}:{self.port} fail",exc_info=True)
        elif mode == 'ssh':
            try:
                self.ssh = paramiko.SSHClient()
                self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.ssh.connect(hostname=self.ip, port=int(
                    self.port), username=self.user, password=self.passwd)
            except Exception:
                logger.error(f"connect {mode}@{self.ip}:{self.port} fail",exc_info=True)

    def bash(self, cmd):
        """
        执行命令
        :param cmd: 传入命令,eg: whoami
        :return 成功返回执行结果,失败返回False
        """
        try:
            _, stdout, stderr = self.ssh.exec_command(cmd)
            res, err = stdout.read(), stderr.read()
            result = res if res else err
            return result.decode()
        except:
            logger.error(f"{self.user}@{self.ip}:{self.port} run '{cmd}' fail",exc_info=True)
            return False

    def put(self, s_file, d_file):
        """
        上传文件
        :param s_file: 传入要上传的文件,eg: ./test.txt
        :param d_file: 远程位置,eg: /tmp/test.txt
        :return 成功返回True,失败返回False
        """
        try:
            self.sftp.put(s_file, d_file)
            return True
        except:
            logger.error(f"{self.user}@{self.ip}:{self.port} upload {s_file}->{d_file} fail",exc_info=True)
            return False

    def get(self, s_file, d_file):
        """
        下载文件
        :param s_file: 远程文件位置,eg: /tmp/test.txt
        :param d_file: 下载存储位置,eg: ./test.txt
        :return 成功返回True,失败返回False
        """
        try:
            self.sftp.get(s_file, d_file)
            return True
        except Exception:
            logger.error(f"{self.user}@{self.ip}:{self.port} download {s_file}->{d_file} fail",exc_info=True)
            return False

    def close(self):
        if self.transport:
            self.transport.close()
        if self.sftp:
            self.sftp.close()
        if self.ssh:
            self.ssh.close()

    def __del__(self):
       self.close()
