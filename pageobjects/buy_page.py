#!/usr/bin/python3
# _*_ coding:utf-8 _*_
from time import sleep
from selenium.webdriver.common.keys import Keys
from test_unittest_demo.pageLocators import buy_ticket_locators
class Buy():
    def __init__(self,driver):
        self.driver=driver
    def cha_xun(self,chu_fa,dao_da):
        departure=self.driver.find_element_by_xpath(buy_ticket_locators.Buy_ticker.buy_departure)
        sleep(2)
        departure.click()
        departure.send_keys(chu_fa)
        departure.send_keys(Keys.ENTER)
        # 到达地选择
        arrival_point = self.driver.find_element_by_xpath(buy_ticket_locators.Buy_ticker.buy_arrival)
        sleep(2)
        arrival_point.click()
        arrival_point.send_keys(dao_da)
        arrival_point.send_keys(Keys.ENTER)
        # 高铁，动车选择
        elect = self.driver.find_element_by_xpath(buy_ticket_locators.Buy_ticker.buy_elect)
        elect.click()
        # 查询
        query = self.driver.find_element_by_xpath(buy_ticket_locators.Buy_ticker.buy_query)
        query.click()
        # # 预定
        # self.driver.maximize_window()
        # hands = self.driver.window_handles
        # print(hands)
        # self.driver.switch_to.window(hands[1])
        # print(self.driver.title)
        # sleep(2)
        # reserve = self.driver.find_element_by_xpath(buy_ticket_locators.Buy_ticker.buy_reserve)
        # reserve.click()

