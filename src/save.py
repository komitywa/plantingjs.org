# -*- coding: utf-8 -*

u"""
module: save
"""

import json

from flask import request

def save():
    print request.form
    return json.dumps({
        'url': u'https://maps.google.com/'
    })
