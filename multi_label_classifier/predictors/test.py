import json
import os
from predict import Predictor


with open(os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "config/textcnn_config.json"), "r") as fr:
    config = json.load(fr)

predictor = Predictor(config)

#text = "please see the content of this report"
text = "the relation between pearson 's correlation coefficient and salton 's cosine measure is revealed based on the different possible values of the division of the l1 norm and the l2 norm of a vector these different values yield a sheaf of increasingly straight lines which form together a cloud of points , being the investigated relation the theoretical results are tested against the author co citation relations among 24 informetricians for whom two matrices can be constructed , based on co citations the asymmetric occurrence matrix and the symmetric co citation matrix both examples completely confirm the theoretical results the results enable us to specify an algorithm which provides a threshold value for the cosine above which none of the corresponding pearson correlations would be negative using this threshold value can be expected to optimize the visualization of the vector space"
result = predictor.predict(text.split(" "))
print(text.split(" "))
print(result)

