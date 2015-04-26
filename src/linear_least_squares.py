__author__ = 'patrickemami'


import os,csv,numpy as np
import random

CONFIG_DIR = 'config'
DATA_STORE = 'iris.data.txt'
NUMBER_OF_ATTRIBUTES = 4

CLASS_1 = 'Iris-setosa'
CLASS_n1 = 'Iris-versicolor'

TRAINING_SET = 20

dir = os.path.dirname(__file__)
cfg_file = os.path.join(dir, '..', CONFIG_DIR, DATA_STORE)

def parse():
    data = []
    with open(cfg_file, "r") as f:
        reader = csv.reader(f)
        for line in reader:
            data.append(list(line))
    return data

# Create a matrix whose columns are vectors of features
# an extra dimension is added to each feature vector by the addition of a 1.0
def do_feature_vector(data):
    global NUMBER_OF_INSTANCES
    x = []
    for row in data[:NUMBER_OF_INSTANCES]:
        list_of_floats = [float(_) for _ in row[:NUMBER_OF_ATTRIBUTES]]
        x.append([1.0] + list_of_floats)
    return x


def classify(v):#Assigns a value of -1 or 1 to each class
    classes = []
    not_used = []
    for _ in v:
        if _[-1] == CLASS_1:
            classes.append(1)
        elif _[-1] == CLASS_n1:
            classes.append(-1)
        else:
            not_used.append(0)
    return classes


def linear_least_squares(x, y):
    x = np.asmatrix(x)
    y = np.array(y)

    left_matrix = np.sum((x_i.T * x_i for x_i in x), axis=0)

    # Try to calculate inverse of left_matrix
    try:
        left_matrix_inv = np.linalg.inv(left_matrix)
    # If it fails, add a tiny identity matrix to make it invertible
    except np.linalg.LinAlgError:
        left_matrix_inv = np.linalg.inv(left_matrix + 0.0001*np.identity(left_matrix.ndim()))

    right_matrix = np.sum(y[idx] * x_i for idx, x_i in enumerate(x))

    return left_matrix_inv * right_matrix.T

def rescale(mat):#Scales any n x m matrix to the range [-1 1] if all the values inside are floats
    mat_rot = np.rot90(mat)
    for idx,col in enumerate(mat_rot):
        max = np.amax(col)
        min = np.amin(col)
        if max != min:
            mat_rot[idx,:] = (col-min)/(max-min)*2-1
        else:
            mat_rot[idx,:] = (col/max)
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
    global NUMBER_OF_INSTANCES
    data = parse()
    y = classify(data)

    # If not all of the classes in the data set were used, this will update our global variable
    NUMBER_OF_INSTANCES = y.__len__()

    x = rescale(do_feature_vector(data))
    w = linear_least_squares(x, y)
    x_svm = svmTransform(data)

    print x_svm
