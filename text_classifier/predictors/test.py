import json
import jieba
from predict import Predictor
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--config_path", help="config path of model")
args = parser.parse_args()

print("path_>" + os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), args.config_path))

with open(os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), args.config_path), "r", encoding="utf8") as fr:
    config = json.load(fr)

with open("../data/hais/hais_2020-01-01_2020-06-30.txt", "r", encoding="utf8") as f:
    data = [line for line in f.readlines()]
    inputs = []
    labels = []
    for line in data:
        try:
            x, y = line.strip().split("<SEP>")
            inputs.append(x.strip())
            labels.append(y.strip())
        except:
            print(line)

# text = " ".join([" ".join(jieba.lcut(line)) for line in data])

predictor = Predictor(config)

total = len(labels)
corr = 0
for i in range(len(inputs)):
    result = predictor.predict(inputs[i].split(" "))
    print("------------------------------------")
    print("result" + str(result) + " labels" + str(labels[i]))
    if str(result) == str(labels[i]):
        corr += 1
    else:
        print(inputs[i])
    print(i, corr, total)
print(corr / total)
