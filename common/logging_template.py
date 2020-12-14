#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author ：啊志
# @Time：2019/10/11 14:39

import logging


class MyLogging(object):
    # 自己封装的日志类
    def __init__(self):
        # 创建自己的日志收集器
        self.my_log = logging.getLogger('my_log')
        self.my_log.setLevel('DEBUG')
        # 创建一个日志输出渠道（输出到控制台）
        l_s = logging.StreamHandler()
        l_s.setLevel('WARNING')
        # 创建一个日志输出渠道（输出到文件）
        l_f = logging.FileHandler(r'D:\python\python代码\test_unittest_demo\output\log\login.log', encoding='utf8')
        l_f.setLevel('DEBUG')
        # 将输出渠道添加到日志收集器中
        self.my_log.addHandler(l_s)
        self.my_log.addHandler(l_f)

        # 设置日志输出的格式
        ft = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        ft = logging.Formatter(ft)
        # 设置日志输出的格式
        l_s.setFormatter(ft)
        l_f.setFormatter(ft)

    def debug(self, msg):
        self.my_log.debug(msg)

    def info(self, msg):
        self.my_log.info(msg)

    def warning(self, msg):
        self.my_log.warning(msg)

    def error(self, msg):
        self.my_log.error(msg)

    def critical(self, msg):
        self.my_log.critical(msg)



