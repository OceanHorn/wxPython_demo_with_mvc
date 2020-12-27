#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: GuoYufu
@license: Apache Licence 
@contact: OceanHorn@163.com
@software: PyCharm
@file: main.py
@time: 2020/12/27 2:13
"""
from controller import Controller

"""
An example of a Model-View-Controller architecture,
using wx.lib.pubsub to handle proper updating of widget (View) values.
"""
import wx

if __name__ == "__main__":
    app = wx.App(False)
    controller = Controller(app)
    app.MainLoop()
