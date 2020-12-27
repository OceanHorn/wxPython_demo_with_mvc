#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: GuoYufu
@license: Apache Licence 
@contact: OceanHorn@163.com
@software: PyCharm
@file: model.py
@time: 2020/12/27 19:27
"""
from pubsub import pub


class Model:
    def __init__(self):
        self.myMoney = 0

    def add_money(self, value):
        self.myMoney += value
        # now tell anyone who cares that the value has been changed
        pub.sendMessage("MONEY.CHANGED", money=self.myMoney)

    def remove_money(self, value):
        self.myMoney -= value
        # now tell anyone who cares that the value has been changed
        # pub.sendMessage("MONEY CHANGED", money=myMoney)
        pub.sendMessage('MONEY.CHANGED', money=self.myMoney)
