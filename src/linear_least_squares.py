__author__ = 'patrickemami'

import os, csv

CONFIG_DIR = 'config'
DATA_STORE = 'iris.data.txt'

CLASS_1 = 'Iris-setosa'
CLASS_n1 = 'Iris-versicolor'

dir = os.path.dirname(__file__)
cfg_file = os.path.join(dir, '..', CONFIG_DIR, DATA_STORE)

def parse():
    with open(cfg_file, "r") as f:
        data = csv.reader(f)
#        for _ in data:
#            print _
        return data

def classify(v):
    for _ in v:
        if _[-1] == CLASS_1:
            _[-1] = 1
        elif _[-1] == CLASS_n1:
            _[-1] = -1
        else:
            _[-1] = 0
    return v

if __name__ == '__main__':
    parsed = parse()
    #classify(parsed)