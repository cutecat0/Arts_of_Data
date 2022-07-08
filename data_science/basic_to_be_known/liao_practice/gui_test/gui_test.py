#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from tkinter import *
import tkinter.messagebox as messagebox

logging.getLogger().setLevel(logging.INFO)


def test():
    """
    Tk, wxWidgets, Qt, GTK
    BUT, python owns Tkinter which supports Tk
    :return:
    """


# 第二步是从Frame派生一个Application类，
# 这是所有Widget的父容器：
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.heyLabel = Label(self, text='Hey, lovely cat！')
        self.nameInput = Entry(self)
        self.heyLabel.pack()
        # self.quitBotton = Button(self, text='Quit', command=self.quit)
        # self.quitBotton = Button(self, text='Hey', command=self.hey)
        # self.quitBotton.pack()
        self.alertButton = Button(self, text='Hey', command=self.hey)
        self.alertButton.pack()

    def hey(self):
        name = self.nameInput.get() or 'cat'
        messagebox.showinfo('Message', 'Hey, %s' % name)


if __name__ == '__main__':

    app =Application()
    app.master.title('Hey, cat')
    app.mainloop()
