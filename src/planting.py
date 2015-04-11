# -*- coding: utf-8 -*-

u"""
module: planting
"""

from flask import Flask
from flask import render_template

from save import save


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/callback')
def callback():
    return render_template('save_callback.html')


save = app.route('/save', methods=['POST'])(save)


if __name__ == '__main__':
    app.run()
