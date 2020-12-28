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


"""
An example of a Model-View-Controller architecture,
using wx.lib.pubsub to handle proper updating of widget (View) values.
"""
import wx

def mvc_with_pypubsub():
    from with_pypubsub.controller import Controller
    app = wx.App(False)
    controller = Controller(app)
    app.MainLoop()

def mvc_with_pydispatcher():
    app = wx.App(False)
    from with_pydispatcher.controller import Controller
    controller = Controller(app)
    app.MainLoop()

if __name__ == "__main__":
    # mvc_with_pypubsub()
    mvc_with_pydispatcher()
