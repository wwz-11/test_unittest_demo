#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author ：大熊
# @Time：2019/5/28 23:45
# @Software：求索教育
# @Email:122712084@qq.com


import os
def get_cwd():
    path = os.path.dirname(os.path.abspath(__file__))

    print(path)
    #当前文件的绝对路径

    return path
if __name__=="__main__":
    get_cwd()

