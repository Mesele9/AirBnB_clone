#!/usr/bin/env python3
''' Initializes module
'''
import sys

sys.path.append("/home/vagrant/AirBnB_clone/models")

import models.engine.file_storage as fs


storage = fs.FileStorage()

storage.reload()
