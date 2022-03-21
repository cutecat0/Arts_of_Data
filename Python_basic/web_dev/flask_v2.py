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
    :return:
    '''
    return render_template('home.html')


@app.route('/signin', methods='[GET]')
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods='[POST]')
def signin():
    username = request.form['username']
    pwd = request.form['password']
    if username == 'admin' and pwd == 'password':
        return render_template('sign_ok.html', username=username)
    return render_template('form.html', message='Wrong username or password. Please sign again!')


if __name__ == '__main__':
    app.run()