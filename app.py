# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from flask import Flask, request, abort

app = Flask(__name__)


@app.route("/", methods=['GET'])
def basic_url():
    return 'hello'


if __name__ == "__main__":
    app.run()
