#!/usr/bin/python3
# _*_ coding:utf-8 _*_
# 设置日志存放路径，日志文件名
# 获取本地时间，转换为设置的格式
import os
import time
from test_unittest_demo import getcwd


def path_1():
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    # 设置所有日志和错误日志的存放路径
    path = getcwd.get_cwd()
    # 通过getcwd.py文件的绝对路径来拼接日志存放路径
    all_path = os.path.join(path, 'output/report/')

    # 设置日志文件名
    all_name = all_path + rq + '.html'
    return all_name
