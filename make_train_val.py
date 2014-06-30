import os
from random import shuffle

train_dir = 'train/'
filenames = [fn for fn in os.listdir(train_dir)]

shuffle(filenames)

labels = []
for fn in filenames:
    if fn.split('.')[0] == 'dog':
        labels.append(1)
    else:
        assert fn.split('.')[0] == 'cat'
        labels.append(0)


Nval = 0
with open('dc_val2.txt', 'w') as fd:
    for fn, lb in zip(filenames[:Nval], labels[:Nval]):
        fd.write(fn + ' ' + str(lb) + '\n')

with open('dc_train2.txt', 'w') as fd:
    for fn, lb in zip(filenames[Nval:], labels[Nval:]):
        fd.write(fn + ' ' + str(lb) + '\n')

    
