import numpy as np
import os
import random

train_data_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "hais/lilian_train_resample.txt")
data_eval_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "hais/eval_data.txt")
data_train_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "hais/train_data.txt")
data_eval = []
data_train = []
k = 3
m = 20
with open(train_data_path, "r", encoding="utf8") as fr:
    for line in fr.readlines():
        if np.random.randint(1, 5, dtype='int') == k:
            data_eval.append(line)
        else:
            data_train.append(line)

random.shuffle(data_train)
random.shuffle(data_eval)

print(type(data_eval))
print(len(data_eval))
print(len(data_train))

if not os.path.exists(data_eval_path):
    with open(data_eval_path, "w", encoding="utf8") as fr_eval:
        for line in data_eval:
            fr_eval.writelines(line)
if not os.path.exists(data_train_path):
    with open(data_train_path, "w", encoding="utf8") as fr_train:
        for line in data_train:
            fr_train.writelines(line)
