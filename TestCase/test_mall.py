#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Common import read_excel
from Common.baseui import baseUI
from Common.read_excel import read_excel_list


class TestMall:
    @pytest.mark.smoke
    def test_login(self,driver):
        # 确定chromedriver.exe的位置
        driver_path = os.path.join(os.path.dirname(__file__), "../chromedriver/chromedriver.exe")
        # 打开浏览器
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()  # 最大化浏览器
        driver.set_page_load_timeout(10)  # 网页加载超时为10s
        driver.set_script_timeout(10)  # js脚本运行超时10s
        driver.implicitly_wait(10)  # 元素查找超时时间10s
        base = baseUI(driver)

        # 打开网址
        driver.get('http://192.168.1.137/#/login')
        # 定位用户名输入框
        # username = driver.find_element_by_xpath("//input[@name='username']")
        base.click("点击登录按钮","(//span[contains(text(),'登录')])[1]")


        #输入用户名
        # username.send_keys("admin")

        # 定位密码输入框//input[@name='password']
        # password = driver.find_element_by_xpath("//input[@name='password']")
        # 输入密码
        # password.send_keys("123456")
        # 定位登录按钮//span[contains(text(),'登录')]

        # driver.find_element_by_xpath("(//span[contains(text(),'登录')])[1]").click()
        # 点击登录按钮
        try:
            # driver.find_element_by_xpath("//span[contains(text(),'残忍拒绝')]").click()
            base.click("点击残忍拒绝","//span[contains(text(),'残忍拒绝')]").click()
        except:
            pass
        time.sleep(2)
        base.click("点击登录按钮", "(//span[contains(text(),'登录')])[1]")
        # driver.find_element_by_xpath("(//span[contains(text(),'登录')])[1]").click()
        time.sleep(1)
        assert '首页'in driver.page_source
        pass
    def test_find_order(self,driver):
        print('查询订单')
        pass

    l_name = read_excel_list('d:\name.xlsx')
    @pytest.fixture(params=l_name)
    def name(self,request):
        return request.param



