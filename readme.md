**pyUITest Readme**
~~~~
项目结构：
Page/:存放page层的封装。
TestDir/:测试用例目录。
TestReport/:测试报告目录。
conftest.py:pytest配置文件。
run_tests.py:测试运行文件。
~~~~
**命名规范**
~~~~
1、对于page层的封装存放于page/目录，命名规范为“xxx_page.py”。
2、对于测试用例的编写存放于test_dir/目录，命名规范为“test_xxx.py”。
3、每一个功能点对于一个测试类，并且以“Test”开头，如“TestLogin”、“TestOrder”等。
4、在一个测试类下编写功能点的所有的测试用例，如“test_login_user_null”、“test_login_success”等。
~~~~
**安装依赖**
~~~~
pip install -r ***.txt
~~~~