#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/11 15:30
# @Author  : nishiting
# @File    : __init__.py.py
# @Description:
__config__ = {
    # 股票最小手续费，单位元
    "cn_stock_min_commission": 5,
    # 佣金倍率（即将废弃）
    "commission_multiplier": None,
    # 股票佣金倍率,即在默认的手续费率基础上按该倍数进行调整，股票的默认佣金为万八
    "stock_commission_multiplier": 1,
    # 期货佣金倍率,即在默认的手续费率基础上按该倍数进行调整，期货默认佣金因合约而异
    "futures_commission_multiplier": 1,
    # 印花倍率，即在默认的印花税基础上按该倍数进行调整，股票默认印花税为千分之一，单边收取
    "tax_multiplier": 1,
}