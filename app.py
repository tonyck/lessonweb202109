from flask_ngrok import run_with_ngrok
from flask import Flask

app = Flask(__name__)  # _name_ 代表目前執行的模組
run_with_ngrok(app)  # starts ngrok when the app is run


@app.route("/")  # 函式的裝飾(Decorator)：以函式為基礎，提供附加的功能
# 撰寫程式
def home():
    return "<h1>Running Flask on Google Colab!</h1>"
