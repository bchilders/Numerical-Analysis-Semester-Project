__author__ = 'patrickemami,tylorchilders'


import os,csv,numpy as np
import random

CONFIG_DIR = 'config'
DATA_STORE = 'iris.data.txt'#'wine.data.txt'
NUMBER_OF_ATTRIBUTES = 4#13
NUMBER_OF_CLASSES = 3

CLASS_1 = 'Iris-setosa'#'1'
CLASS_2 = 'Iris-versicolor'#'2'
CLASS_3 = 'Iris-virginica'#'3'

CLASS_POS = -1#0

TRAINING_SET_PERCENT = 30

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
    x = []
    for row in data[:]:
        list_of_floats = [float(_) for _ in row[CLASS_POS+1:CLASS_POS+1+NUMBER_OF_ATTRIBUTES]]
        x.append([1.0] + list_of_floats)
    return x


def classify(v):#Assigns a value of -1 or 1 to each class
    classes = []
    for _ in v:
        if _[CLASS_POS] == CLASS_1:
            classes.append([1, 0, 0])
        elif _[CLASS_POS] == CLASS_2:
            classes.append([0, 1, 0])
        elif _[CLASS_POS] == CLASS_3:
            classes.append([0, 0, 1])
    return classes


def linear_least_squares(x, y):
    x = np.asmatrix(x)
    y = np.matrix(y)

    left_matrix = np.sum((x_i.T * x_i for x_i in x), axis=0)

    # Try to calculate inverse of left_matrix
    try:
        left_matrix_inv = np.linalg.inv(left_matrix)
    # If it fails, add a tiny identity matrix to make it invertible
    except np.linalg.LinAlgError:
        left_matrix_inv = np.linalg.inv(left_matrix + 0.0001*np.identity(left_matrix.shape[0]))

    right_matrix = np.asmatrix(np.zeros((NUMBER_OF_CLASSES,NUMBER_OF_ATTRIBUTES+1)))

    for idx, x_i in enumerate(x):
        right_matrix = right_matrix + np.asmatrix((y)[idx].T*x_i)

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

def train(data,num):
    trainset = random.sample(data,num)

    for _ in trainset:
        data.remove(_)

    y = classify(trainset)

    x = rescale(do_feature_vector(trainset))
    w = linear_least_squares(x, y)
    return w

def test(w,data):
    x=rescale(do_feature_vector(data))
    result = x*w
    return result

if __name__ == '__main__':
    data = parse()

    w = train(data,int(((TRAINING_SET_PERCENT/100.0)*data.__len__())))

    t = random.sample(data,data.__len__())

    results = test(w,t)

    p = 0

    #print results

    for i,r in enumerate(results):
        v = np.matrix.argmax(np.abs(r))
        if v == 0 and t[i][CLASS_POS] == CLASS_1:
            print "Good"
            p = p+1.0
        elif v == 1 and t[i][CLASS_POS] == CLASS_2:
            print "Good"
            p = p+1.0
        elif v == 2 and t[i][CLASS_POS] == CLASS_3:
            print "Good"
            p = p+1.0
        else:
            print "Bad"
    print p/data.__len__()*100.0