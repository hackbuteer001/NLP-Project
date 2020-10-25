import os
from collections import Counter

_train_data_path = "/home/caoyu/project/NLP-Project/text_classifier/data/hais/train_data.txt"
print(_train_data_path)
inputs = []
labels = []
with open(_train_data_path, "r", encoding="utf8") as fr:
    for line in fr.readlines():
        try:
            text, label = line.strip().split("<SEP>")
            inputs.append(text.strip().split(" "))
            labels.append(label)
        except:
            continue
print(Counter(labels))