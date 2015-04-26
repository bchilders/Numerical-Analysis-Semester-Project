__author__ = 'patrickemami'

import os, csv

CONFIG_DIR = 'config'
DATA_STORE = 'iris.data.txt'

dir = os.path.dirname(__file__)
cfg_file = os.path.join(dir, '..', CONFIG_DIR, DATA_STORE)

def parse():
    with open(cfg_file, "r") as f:
        data = csv.reader(f)
        return data

if __name__ == '__main__':
    parse()