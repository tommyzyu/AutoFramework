#!/usr/local/bin/python3.9
# coding=utf-8
"""
登录类
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from common import config


class LoginPage(BasePage):
    # 封装页面元素，统一管理
    file_path = "./data/url.ini"
    config_list = config.read_config(file_path)
    current_url = config_list[0][1]
    username_loc = (By.XPATH, '//*[@id="custom-validation_username"]')
    password_loc = (By.XPATH, '//*[@id="custom-validation_password"]')
    submit_loc = (By.XPATH, '//*[@id="app"]/div/div/div/div[3]/div/div/div[3]/div/div/div/button')

    # 封装页面动作，统一管理
    def login_ecshop(self, username, password):
        self.get(self.current_url)
        self.send_keys(self.username_loc, username)
        self.send_keys(self.password_loc, password)
        self.click(self.submit_loc)