#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import logging

logging.getLogger().setLevel(logging.INFO)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    '''
    use template then pass parameters in template html
    which is MVC : Model-View-Controller
    use Jinja2 as html template in this eg

    除了Jinja2，常见的模板还有：
    Mako：用<% ... %>和${xxx}的一个模板；
    Cheetah：也是用<% ... %>和${xxx}的一个模板；
    Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。
    小结
    有了MVC，我们就分离了Python代码和HTML代码。HTML代码全部放到模板里，写起来更有效率。
    :return:
    '''
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    pwd = request.form['password']
    if username == 'admin' and pwd == 'password':
        return render_template('sign_ok.html', username=username)
    return render_template('form.html', message='Wrong username or password. Please sign again!')


if __name__ == '__main__':
    app.run()