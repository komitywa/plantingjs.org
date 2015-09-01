# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from planting import app as application

application.config['PROPAGATE_EXCEPTIONS'] = True
