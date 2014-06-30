'''
import os
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.utils import shuffle

from caffe import imagenet
MODEL_FILE = 'catsdogs_deploy.prototxt'
#PRETRAINED = 'caffe_imagenet_train_iter_5000'
PRETRAINED = 'caffe_imagenet_train_iter_10000_3'

net = imagenet.ImageNetClassifier(MODEL_FILE, PRETRAINED, num_output=2)
net.caffenet.set_mode_gpu()
net.caffenet.set_phase_test()

y_hat = []
for idx in range(12500):
    print idx
    y_hat.append(net.predict('test1/' + str(idx+1) + '.jpg'))

y_hat = np.vstack(y_hat)
y = y_hat.argmax(axis=1)

with open('pred_4.csv','w') as fd:
    fd.write('id,label\n')
    for idx in range(len(y)):
        fd.write(str(idx+1) + ',' + str(y[idx]) + '\n')

with open('pred_4_prob.csv','w') as fd:
    fd.write('id,label\n')
    for idx in range(len(y)):
        fd.write(str(idx+1) + ',' + str(y_hat[idx][0]) + '\n')
'''

with open('submission2.csv','w') as fd:
    fd.write('id,label\n')
    for idx in range(len(y)):
        fd.write(str(idx+1) + ',' + str(int(round(1.0-y[idx][1]))) + '\n')
