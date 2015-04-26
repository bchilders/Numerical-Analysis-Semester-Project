__author__ = 'patrickemami'

import os,csv,numpy as np

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

def classify(v):#Assigns a value of -1 or 1 to each class
    classes = []
    for _ in v:
        if _[-1] == CLASS_1:
            classes.append(1)
        elif _[-1] == CLASS_n1:
            classes.append(-1)
        else:
            classes.append(0)
    return classes

def rescale(mat):#Scales any n x m matrix to the range [-1 1] if all the values inside are floats
    mat_rot = np.rot90(mat)
    for idx,col in enumerate(mat_rot):
        max = np.amax(col)
        min = np.amin(col)
        mat_rot[idx,:] = (col-min)/(max-min)*2-1
    return np.rot90(mat_rot,3)

def svmTransform(data):
    svmout = []
    y = classify(data)
    ysvm = []
    for _ in y:
        if _ == -1:
            ysvm.append('-1')
        elif _ == 1:
            ysvm.append('+1')
    for row in data:
        fil_row = row[:NUMBER_OF_ATTRIBUTES]
        form_row = []
        for idx,ent in enumerate(fil_row):
            form_row.append(str(idx+1)+':'+ent)
        svmout.append([ysvm[idx]]+form_row)
    return svmout




if __name__ == '__main__':
    data = parse()
    x = svmTransform(data)
    print x
