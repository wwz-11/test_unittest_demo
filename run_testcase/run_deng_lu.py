#!/usr/bin/python3
# _*_ coding:utf-8 _*_
# @Author:啊志
# @Time:2019/9/23 9:20
# @Email:1427245437@qq.com
import  unittest
from HTMLTestRunnerNew import HTMLTestRunner

from deng_lu_unittist_ddt import deng_lu_ddt
suite=unittest.TestSuite()
loder=unittest.TestLoader()
suite.addTest(loder.loadTestsFromTestCase(deng_lu_ddt.deng_lu_ddt_tset))
with open('1.html','wb' ) as f:
    test=HTMLTestRunner(
                        stream=f,
                       verbosity=4,                #详细程度
                       title='我的第一份测试报告',
                       description="第一份测试报告",
                       tester="啊志")
    test.run(suite)

