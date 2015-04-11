# -*- coding: utf-8 -*

u"""
module: save
"""

import json


def save():
    return json.dumps({
        'url': u'https://maps.google.com/'
    })
