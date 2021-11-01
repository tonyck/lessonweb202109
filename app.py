# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from flask import Flask, request, abort

app = Flask(__name__)


@app.route("/", methods=['GET'])
def basic_url():
    return '<h1>賴田捕手第 20 天</h1><p>全身都是肌肉沒半點腦子。反正，那就是鄭尼那晚照顧的草泥馬。我完全無法了解，我發誓我沒辦法。</p>'


if __name__ == "__main__":
    app.run()
