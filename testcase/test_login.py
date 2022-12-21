# coding = "UTF-8"
# 测试用例层
from cProfile import run
from tkinter import N

import allure
import pytest
from selenium import webdriver
from common.excel_util import read_excel
from pageobject.login_page import LoginPage

class TestLogin:

    def setup_class(self):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(5)

    # 登录系统
    @pytest.mark.parametrize("caseinfo", read_excel("./data/test_login.xlsx", "test_01_login", 5))
    def test_01_login(self, caseinfo):
        try:
            loginpage = LoginPage(self.driver)
            loginpage.login_ecshop(caseinfo[2], caseinfo[3])

        except Exception as e:
            # 保存错误截图
            file_name = r'C:\Users\admin\Desktop\PythonUI\error_image\logo.png'
            self.driver.save_screenshot(file_name)
            # 把错误截图以附件的形式加载到allure报告中
            with open(file_name, mode='rb') as f:
                allure.attach(f.read(), 'logo.png', allure.attachment_type.PNG)
