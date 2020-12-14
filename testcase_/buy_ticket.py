#!/usr/bin/python3
# _*_ coding:utf-8 _*_
import unittest
from selenium import webdriver
from test_unittest_demo.pageobjects import buy_page
class Buy_ticket(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.12306.cn/index/index.html")
    def tearDown(self):
        self.driver.quit()
    def test_buy_ticket(self):
        buy_page.Buy(self.driver).cha_xun("长沙南","上海南")

