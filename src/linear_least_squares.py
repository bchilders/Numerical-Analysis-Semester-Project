__author__ = 'patrickemami'

import os, csv

CONFIG_DIR = 'config'
DATA_STORE = 'iris.data.txt'
NUMBER_OF_ATTRIBUTES = 4
NUMBER_OF_INSTANCES = 150

dir = os.path.dirname(__file__)
cfg_file = os.path.join(dir, '..', CONFIG_DIR, DATA_STORE)

def parse():
    data = []
    with open(cfg_file, "r") as f:
        reader = csv.reader(f)
        for line in reader:
            data.append(list(line))
    print data
    return data

def do_feature_vector(data):
    x = []
    for row in data:
        list_of_floats = [float(_) for _ in row[:NUMBER_OF_ATTRIBUTES]]
        x.append([1.0] + list_of_floats)
    return x

if __name__ == '__main__':
    data = parse()
    x = do_feature_vector(data)
    print x