#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : operate_login_page.py 
@Contact : android4google@163.com
@MTime : 2019/11/13 15:51 
@Author: zhangyun
@Version: 1.0
@Description: 运营平台登录页面page封装层
"""

from poium import Page, PageElement


class OperateLoginPage(Page):
    login_phone = PageElement(id_='username', describe='账户输入框')
    login_password = PageElement(id_='password', describe='密码输入款')
    login_button = PageElement(xpath="//*[@class='btns-lock']", describe='登录按钮')
