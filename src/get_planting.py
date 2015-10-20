# -*- coding: utf-8 -*

u"""
module: get_planting
"""

import sqlite3

from flask import jsonify

from create_db import db_path


GET_PLANTING = """
SELECT * FROM plantings where id={}
"""

GET_OBJECTS = """
SELECT * FROM objects where id={}
"""


class PlantingObject(object):

    def __init__(self, object_row):
        self.object = object_row[1]
        self.projection = object_row[2]
        self.width = object_row[3]
        self.position = {
            "x": object_row[4],
            "y": object_row[5]
        }
        self.layer = object_row[6]


class Planting(object):

    def __init__(self, id_):
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        planting = c.execute(GET_PLANTING.format(id_)).fetchone()
        self.manifesto = planting[1]
        self.lat = planting[2]
        self.lng = planting[3]
        self.heading = planting[4]
        self.pitch = planting[5]
        self.zoom = planting[6]
        self.objects = [
            PlantingObject(row) for row in c.execute(GET_OBJECTS.format(id_))
        ]
        conn.close()


def get_planting(path):
    request_id = path
    planting = Planting(id_=request_id)
    return jsonify(**{
        "manifesto": planting.manifesto,
        "lat": planting.lat,
        "lng": planting.lng,
        "heading": planting.heading,
        "pitch": planting.pitch,
        "zoom": planting.zoom,
        "objects": [
            {
                "object": obj.object,
                "projection": obj.projection,
                "width": obj.width,
                "position": {
                    "x": obj.position['x'],
                    "y": obj.position['y']
                }
            }
            for obj in planting.objects
        ]
    })
