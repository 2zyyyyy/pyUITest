#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : test_allure_report.py
@Contact : android4google@163.com
@MTime : 2019/12/13 15:22 
@Author: zhangyun
@Version: 1.0
@Description: 测试生成Allure测试报告
"""

import os


def test_01():
    assert 1 == 1


def test_02():
    assert 1 + 1 == 2


if __name__ == '__main__':
    pytest.main(["--alluredir Report Common"])
    os.popen("allure generate Report\\ -o Allure\\ --clean")
