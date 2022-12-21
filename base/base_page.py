#!/usr/local/bin/python3.9
# coding=utf-8
"""
基础层，存放原生方法

"""

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
    
    # 打开网页
    def get(self, url):
        self.driver.get(url)
    # 封装定位
    def locator_element(self, args):
        return self.driver.find_element(*args)
    
    # 封装一个输入值
    def send_keys(self, args, value):
        self.locator_element(args).send_keys(value)
    
    # 封装点击动作
    def click(self, args):
        self.locator_element(args).click()
        
    # 清楚输入框内容
    def clear(self, args):
        self.locator_element(args).clear()
        
    # 进入框架
    def goto_frame(self, frame_name):
        self.driver.switch_to.frame(frame_name)
    
    # 跳出框架
    def out_frame(self):
        self.driver.switch_to.default_content()
    
    # 选择下拉框
    def choice_select(self):
        pass