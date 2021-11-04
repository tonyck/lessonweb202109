# -*- coding: utf-8 -*-


from __future__ import unicode_literals
# 引入套件
from flask import Flask, request, abort
# 初始化Flask物件
app = Flask(__name__)


@app.route("/", methods=['GET'])
def basic_url():
    return '<h1>Hello Python!</h1><p>網站架在Heroku上</p>'


@app.route("/map/w01-6", methods=['GET'])
def map_w01_6():
    return app.send_static_file('W01-6.html')


if __name__ == "__main__":
    app.run()
