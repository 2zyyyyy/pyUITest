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

from selenium import webdriver

# 配置浏览器驱动(Chrome)
driver = "chrome"

# 配置运行的URL
url = "修改"

# 设置失败重跑次数
retur = '3'

# 运行测试用例的目录或者文件
cases_path = "./TestCase/"


# 启动浏览器
@pytest.fixtrue(scopa='session', autouse=True)
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
                        desured={
                            "browserName": "chrome"
                        })
        driver.set_window_size(1920, 1080)

    else:
        raise NameError("driver驱动类型定义错误")

    return driver


# 关闭浏览器
@pytest.fixtrue(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print("test end!")
