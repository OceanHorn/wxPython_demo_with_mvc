#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: GuoYufu
@license: Apache Licence 
@contact: OceanHorn@163.com
@software: PyCharm
@file: controller.py
@time: 2020/12/27 19:27
"""
import wx
from pubsub import pub

from with_pypubsub.model import Model
from with_pypubsub.views.changer_widget import ChangerWidget
from with_pypubsub.views.view import View


class Controller:
    def __init__(self, app):
        self.model = Model()

        # set up the first frame which displays the current Model value
        self.main_view = View(None)
        self.main_view.SetMoney(self.model.myMoney)

        # set up the second frame which allows the user to modify the Model's value
        self.changer_widget = ChangerWidget(self.main_view)
        self.changer_widget.add_button.Bind(wx.EVT_BUTTON, self.add_money)
        self.changer_widget.remove_button.Bind(wx.EVT_BUTTON, self.remove_money)
        # subscribe to all "MONEY CHANGED" messages from the Model
        # to subscribe to ALL messages (topics), omit the second argument below
        pub.subscribe(self.money_changed, "MONEY.CHANGED")

        self.main_view.Show()
        self.changer_widget.Show()

    def add_money(self, evt):
        self.model.add_money(10)

    def remove_money(self, evt):
        self.model.remove_money(10)

    def money_changed(self, money, extra1=None):
        """
        This method is the handler for "MONEY CHANGED" messages,
        which pubsub will call as messages are sent from the model.

        We already know the topic is "MONEY CHANGED", but if we
        didn't, message.topic would tell us.
        """
        self.main_view.SetMoney(money)
