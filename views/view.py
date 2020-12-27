#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: GuoYufu
@license: Apache Licence 
@contact: OceanHorn@163.com
@software: PyCharm
@file: view.py
@time: 2020/12/27 19:28
"""
import wx


class View(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="Main View")

        sizer = wx.BoxSizer(wx.VERTICAL)
        text = wx.StaticText(self, label="My Money")
        ctrl = wx.TextCtrl(self)
        sizer.Add(text, 0, wx.EXPAND | wx.ALL)
        sizer.Add(ctrl, 0, wx.EXPAND | wx.ALL)

        self.moneyCtrl = ctrl
        ctrl.SetEditable(False)
        self.SetSizer(sizer)

    def SetMoney(self, money):
        self.moneyCtrl.SetValue(str(money))
