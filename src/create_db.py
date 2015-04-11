# -*- coding: utf-8 -*

u"""
module: create_db
"""

import os
import sqlite3

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
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    object INTEGER,
    projection INTEGER,
    width REAL,
    x REAL,
    y REAL
)
"""


def create_database():
    if os.path.isfile('planting.sqlite'):
        os.remove('planting.sqlite')

    conn = sqlite3.connect('planting.sqlite')
    c = conn.cursor()
    c.execute(plantings_create)
    c.execute(objects_create)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()
