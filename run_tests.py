#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : run_tests.py 
@Contact : android4google@163.com
@MTime : 2019/11/13 15:12 
@Author: zhangyun
@Version: 1.0
@Description: 测试运行文件
"""

import click
import time
import logging
import os
import sys
from conftest import XML_REPORT_DIR, ALLURE_REPORT_DIR
from conftest import cases_path, rerun, max_fail
import pytest

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# def init_env(now_time):
#     """
#     初始化测试报告目录
#     """
#     os.mkdir(REPORT_DIR + now_time)


@click.command()
@click.option('-m', default=None, help="请输入运行模式：run or debug")
def run(m):
    if m is None or m == 'run':
        logger.info("回归模式，开始执行-->")
        logger.info(cases_path)
        # now_time = time.strftime("%Y-%m-%d %H-%M-%S")
        # init_env(now_time)
        args = ['-s', '-q', '--alluredir', './Report/']
        pytest.main(args)
        # os.popen('allure generate %s -o %s' % (XML_REPORT_DIR, ALLURE_REPORT_DIR + ' --clean'))
        logger.info("运行结束，生成测试报告...")
    elif m == "debug":
        print("debug模式运行测试用例：")
        pytest.main(["-v", "-s", cases_path])
        print("运行结束")


if __name__ == '__main__':
    run()