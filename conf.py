#!/usr/bin/python3

import json

def read_conf(fname = 'settings.json'):
    with open(fname, 'r') as f:
        conf = json.load(f)
    return conf
