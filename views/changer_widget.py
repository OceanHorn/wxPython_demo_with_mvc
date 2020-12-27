#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: GuoYufu
@license: Apache Licence 
@contact: OceanHorn@163.com
@software: PyCharm
@file: changer_widget.py
@time: 2020/12/27 19:29
"""
import wx


class ChangerWidget(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="Change Widget")

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.add_button = wx.Button(self, label="Add Money")
        self.remove_button = wx.Button(self, label="Remove Money")
        sizer.Add(self.add_button, 0, wx.EXPAND | wx.ALL)
        sizer.Add(self.remove_button, 0, wx.EXPAND | wx.ALL)
        self.SetSizer(sizer)
