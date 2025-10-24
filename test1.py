# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Flask funguj</h1><p>Funguje</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

