#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib, sys, os

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

passw_hash=hashlib.md5(sys.argv[2]).hexdigest()
username=sys.argv[1]

config=configparser.ConfigParser()
config.add_section("Main")
config.set("Main", "username", username)
config.set("Main", "password", passw_hash)

with open(os.path.expanduser('~/.lscrobbler.ini'), "w") as config_file:
        config.write(config_file)