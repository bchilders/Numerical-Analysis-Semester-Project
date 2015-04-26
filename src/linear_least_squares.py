__author__ = 'patrickemami'

import os, csv

CONFIG_DIR = 'config'
DATA = 'iris.data.txt'

dir = os.path.dirname(__file__)
cfg_file = os.path.join(dir, '..', CONFIG_DIR, DATA)

def init():
    with open(cfg_file, "r") as f:
        dimensions = f.readline().strip().split(',')
        for line in f:
            map_text.append(line.strip())