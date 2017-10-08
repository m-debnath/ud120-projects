#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn import model_selection
features_train, features_test, labels_train, labels_test = model_selection.train_test_split(features, labels,
                                                                                           test_size=0.3,
                                                                                           random_state=42)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

print [pred[ii] * 1. for ii in range(0, len(pred))]
print labels_test
print len([pred[ii] for ii in range(0, len(pred)) if pred[ii] == 1])

pred_not_poi = [0 for ii in range(0, len(pred))]
print pred_not_poi

from sklearn.metrics import accuracy_score
score = accuracy_score(labels_test, pred)
print "score:", round(score, 3)
score = accuracy_score(labels_test, pred_not_poi)
print "score:", round(score, 3)

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

precision = precision_score(labels_test, pred)
print "precision:", round(precision, 3)

recall = recall_score(labels_test, pred)
print "recall:", round(recall, 3)

