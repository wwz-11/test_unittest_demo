#!/usr/bin/python3
# _*_ coding:utf-8 _*_

#登录元素定位
class Login_locator():
    user_login_name=b"account"   #_by_id
    user_login_paswod="//input[@name='password']"  #_by_xpath
    user_login_login="button[id='submit']"  #css_selector
    forget_pwd_pwd="//td/a[@href='/zentao/user-reset.html']"
