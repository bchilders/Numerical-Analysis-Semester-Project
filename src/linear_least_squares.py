__author__ = 'patrickemami'

import os, csv

CONFIG_DIR = 'config'
DATA_STORE = 'iris.data.txt'
NUMBER_OF_ATTRIBUTES = 4
NUMBER_OF_INSTANCES = 150

CLASS_1 = 'Iris-setosa'
CLASS_n1 = 'Iris-versicolor'

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

def classify(v):
    classes = []
    for _ in v:
        if _[-1] == CLASS_1:
            classes.append(1)
        elif _[-1] == CLASS_n1:
            classes.append(-1)
        else:
            classes.append(0)
    return v

if __name__ == '__main__':
    data = parse()
    x = do_feature_vector(data)
    print x

