# -*- coding: utf-8 -*-

u"""
module: planting
"""

from flask import Flask

from save import save


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

save = app.route('/save')(save)


if __name__ == '__main__':
    app.run()
