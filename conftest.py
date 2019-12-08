#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : conftest.py 
@Contact : android4google@163.com
@MTime : 2019/11/13 15:12 
@Author: zhangyun
@Version: 1.0
@Description: pytest 配置文件
"""

import os
import sys
import pytest
from py.xml import html
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options

# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR + "/TestReport/"

# 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
driver_type = "chrome"

# 配置运行的URL
url = "http://operate.civaonline.cn/coms/a/login"

# 设置失败重跑次数
rerun = '3'

# 最大失败次数
max_fail = '5'

# 运行测试用例的目录或者文件
cases_path = sys.path[0] + "\\TestCase\\"


# 定义基本测试环境
@pytest.fixture(scope='function')
def base_url():
    global url
    return url


# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def browser():
    """
    定义全局浏览器驱动
    """
    global driver
    global driver_type

    if driver_type == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
    elif driver_type == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
    elif driver_type == "safari":
        driver = webdriver.Safari()
        driver.set_window_size(1920, 1080)
    elif driver_type == "chrome-headless":
        # chrome 无头模式
        chrome_options = CH_Options()
        chrome_options.add_argument("--headles")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(chrome_options=chrome_options)
    elif driver_type == "firefox-headless":
        # firefox 无头模式
        firefox_options = FF_Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(firefox_options=firefox_options)

    elif driver_type == "grid":
        # 通过远程节点运行
        driver = Remote(command_executor='http://10.2.16.182:4444/wd/hub',
                        desired_capabilities={
                            "browserName": "chrome"
                        })
        driver.set_window_size(1920, 1080)

    else:
        raise NameError("driver驱动类型定义错误")

    return driver


# 关闭浏览器
@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print("test end!")


# 失败截图配置
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     用于向测试用例中添加开始时间、内部注释和失败截图等
#     :param item:
#     :return:
#     """
#     pytest_html = item.congig.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_resuslt()
#     report.description = str(item.function.__doc__)
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call' or report.when == 'setup':
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             cases_path = report.nodeid.replace("::", "_") + ".png"
#             if "[" in case

if __name__ == '__main__':
    print(cases_path)
