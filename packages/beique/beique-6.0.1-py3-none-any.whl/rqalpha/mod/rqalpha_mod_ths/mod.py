#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/11 15:31
# @Author  : nishiting
# @File    : mod.py
# @Description: 同花顺数据源
from rqalpha.interface import AbstractMod
from supermind.api import *
class ThsDataMod(AbstractMod):
    def start_up(self, env, mod_config):
        command.login('mx_693441149', 'stni1234')
        print(get_api_usage())
        command.data_setpath(data_path='C:\\Users\\admin\\Documents\\quant\\data\\ths', migrate=True)
        command.data_ingest(bar_types=['minute'], symbols='000001.SZ')
        command.data_ingest(bar_types=['minute'], symbols='000002.SZ')
        command.data_ingest(bar_types=['minute'], symbols='600519.SH')

    def tear_down(self, code, exception=None):
        pass
