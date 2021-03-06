__author__ = 'patrickemami,tylorchilders'


import sys,os,csv,numpy as np
import random

CONFIG_DIR = 'config'
DATA_STORE = 'wine.data.txt'#'iris.data.txt'
NUMBER_OF_ATTRIBUTES = 13#4

CLASS_1 = '1'#'Iris-setosa'
CLASS_n1 = '2'#'Iris-versicolor'
CLASS_NULL = '3'#'Iris-virginica'

CLASS_POS = 0#-1

TRAINING_SET = 10

dir = os.path.dirname(__file__)
cfg_file = os.path.join(dir, '..', CONFIG_DIR, DATA_STORE)

def parse():
    data = []
    with open(cfg_file, "r") as f:
        reader = csv.reader(f)
        for line in reader:
            if list(line)[CLASS_POS] == CLASS_NULL:
                break
            data.append(list(line))
    return data

# Create a matrix whose columns are vectors of features
# an extra dimension is added to each feature vector by the addition of a 1.0
def do_feature_vector(data):
    x = []
    for row in data[:]:
        list_of_floats = [float(_) for _ in row[:NUMBER_OF_ATTRIBUTES]]
        x.append([1.0] + list_of_floats)
    return x

#removes the class we do not want to consider from the data
def clean_data(data):
    for _ in data:
        if _[CLASS_POS]==CLASS_NULL:
            data.remove(_)

#splits the data into a training set and test set
def split_data(data, num):
    trainset = random.sample(data,num)

    for _ in trainset:
        data.remove(_)
        
    return np.array([trainset,data])

def classify(v):#Assigns a value of -1 or 1 to each class
    classes = []
    not_used = []
    for _ in v:
        if _[CLASS_POS] == CLASS_1:
            classes.append(1)
        elif _[CLASS_POS] == CLASS_n1:
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
        left_matrix_inv = np.linalg.inv(left_matrix + 0.0001*np.identity(left_matrix.shape[0]))

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
    svmout = [None for _ in range(data.__len__())]
    y = classify(data)
    ysvm = []
    for _ in y:
        if _ == -1:
            ysvm.append('-1')
        elif _ == 1:
            ysvm.append('+1')
    print ysvm
    
    for row_idx,row in enumerate(data):#indexed data
        fil_row = row[:NUMBER_OF_ATTRIBUTES]
        form_row = ""
        for idx,ent in enumerate(fil_row):
            form_row=form_row+str(idx+1)+':'+ent+' '
       
        svmout[row_idx]=ysvm[row_idx]#+' '+form_row#changed idx to row_idx
        print row_idx
        print ysvm[row_idx]+' '+form_row
        print svmout[row_idx]
                
    return svmout
    
def write_svm(data, name):
    svmData = svmTransform(data)
    try:
        file = open(name,"w")
        for _ in svmData:
            file.write(_)
            print "hello"
        file.close()
    except:
        print "oh fuck"
        sys.exit(0)

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

def main(loops):
    loop = loops
    if loop < 1:
        loop = 1

    while loop > 0:
        data = parse()
        
        clean_data(data)
        
        print "Training\n"
        write_svm(svmTransform(split_data(data,int(((TRAINING_SET/100.0)*data.__len__())))[0]), "theamazingsquidcrusader")
        print "Testing\n"
        write_svm(svmTransform(split_data(data,int(((TRAINING_SET/100.0)*data.__len__())))[1]), "test")
#        w = train(data,int(((TRAINING_SET/100.0)*data.__len__())))
#
#        t = random.sample(data,data.__len__())
#
#        results = test(w,t)
#
#        p = 0
#
#        for i,r in enumerate(results):
#            if r < 0 and t[i][CLASS_POS] == CLASS_n1:
#                #print "Good"
#                p = p+1.0
#            elif r > 0 and t[i][CLASS_POS] == CLASS_1:
#                #print "Good"
#                p = p+1.0
#            #else:
#                #print "Bad"
#        sys.stdout.write((str)(p/data.__len__()*100.0))
        loop = loop - 1

        if loop > 0:
            sys.stdout.write("\n")

if __name__ == '__main__':
    main(1)