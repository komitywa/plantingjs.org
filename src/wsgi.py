# -*- coding: utf-8 -*-

import os
import sys

activate_this = '/root/.virtualenvs/plantingjs_org/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

sys.path.insert(0, os.path.dirname(__file__))

from planting import app as application  # nopep8
