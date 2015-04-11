# -*- coding: utf-8 -*

u"""
module: save
"""

import json
import sqlite3

from flask import request


def save_planting(conn, planting_data):
    c = conn.cursor()
    c.execute(u"""
        INSERT INTO plantings (
            manifesto,
            lat,
            lng,
            heading,
            pitch,
            zoom
        ) VALUES (
            "%(manifesto)s",
            %(lat)s,
            %(lng)s,
            %(heading)s,
            %(pitch)s,
            %(zoom)s
        )
    """ % planting_data)
    c.execute(u"""SELECT last_insert_rowid() FROM plantings""")
    conn.commit()
    return c.fetchone()[0]



def save_object(conn, planting_id, object_data):
    object_data['id'] = planting_id
    object_data.update(object_data['position'])
    c = conn.cursor()
    c.execute(u"""
        INSERT INTO objects (
            id,
            object,
            projection,
            width,
            x,
            y
        ) VALUES (
            "%(id)s",
            %(object)s,
            %(projection)s,
            %(width)s,
            %(x)s,
            %(y)s
        )
    """ % object_data)
    conn.commit()


def save():
    conn = sqlite3.connect('planting.sqlite')
    planting = request.json
    objects = request.json['objects']

    planting_id = save_planting(conn, planting)
    for o in objects:
        save_object(conn, planting_id, o)

    conn.close()

    return json.dumps({
        'url': u'/planted/' + str(planting_id)
    })
