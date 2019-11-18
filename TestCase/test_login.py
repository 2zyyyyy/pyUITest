#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : test_login.py 
@Contact : android4google@163.com
@MTime : 2019/11/13 18:07 
@Author: zhangyun
@Version: 1.0
@Description: 首页登录测试用例
"""

import sys
from os.path import dirname, abspath
from Page.operate_login_page import OperateLoginPage
import pytest

sys.path.insert(0, dirname(dirname(abspath(__file__))))


class TestLogin:
    """首页登录"""

    def test_operate_login_case(self, browser, base_url):
        """账户登录成功"""
        page = OperateLoginPage(browser)
        page.get(base_url)
        page.driver.maximize_window()
        page.login_phone = '1898984969103'
        page.login_password = '123456'
        page.login_button.click()
        sleep(2)
        assert browser.title == 'Civa运营管理平台'