#!/usr/local/bin/python3.9
# coding=utf-8
import configparser

def read_config(files):
    '''
    用户需要范围配置的时候读取read_config函数，
    函数将会返回一个配置列表
    :param files:
    :return:
    '''
    config = configparser.ConfigParser()
    config.read(files)
    value_list = config.items("webconfig")
    return value_list
