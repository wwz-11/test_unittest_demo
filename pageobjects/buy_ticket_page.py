#!/usr/bin/python3
# _*_ coding:utf-8 _*_
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/index.html")
#出发地选择
Departure=driver.find_element_by_xpath("//input[@id='fromStationText']").send_keys("北京")