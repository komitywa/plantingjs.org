# -*- coding: utf-8 -*

u"""
module: create_db
"""

import os
import sqlite3

here = os.path.dirname(__file__)
db_path = os.path.join(here, u'..', u'..', u'plantings.sqlite')

plantings_create = u"""
CREATE TABLE plantings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    manifesto TEXT,
    lat REAL,
    lng REAL,
    heading REAL,
    pitch REAL,
    zoom REAL
)
"""

objects_create = u"""
CREATE TABLE objects (
    id INTEGER,
    object INTEGER,
    projection INTEGER,
    width REAL,
    x REAL,
    y REAL
)
"""

planting_insert = u"""
    INSERT INTO plantings (
        manifesto,
        lat,
        lng,
        heading,
        pitch,
        zoom
    ) VALUES (
        "/manifesto.json",
        52.403526,
        16.911024,
        -74.8140161725,
        2.474393531,
        1
    )
"""

objects_insert = u"""
        INSERT INTO objects (
            id,
            object,
            projection,
            width,
            x,
            y
        ) VALUES (
            "1",
            0,
            0,
            0.0808625336927,
            0.200539083558,
            0.022371967655
        ), (
            "1",
            0,
            4,
            0.0808625336927,
            0.620485175202,
            0.0315363881402
        )
"""


def create_database():
    if os.path.isfile(db_path):
        os.remove(db_path)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(plantings_create)
    c.execute(objects_create)
    c.execute(planting_insert)
    c.execute(objects_insert)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()
