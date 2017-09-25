#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
print "K Nearest Neighbors"
from sklearn.neighbors import KNeighborsClassifier
clf_knn = KNeighborsClassifier(n_neighbors=3, algorithm='auto')
t0 = time()
clf_knn.fit(features_train, labels_train)
print "training time knn:", round(time()-t0, 3), "s"
t0 = time()
pred_knn = clf_knn.predict(features_test)
print "predict time knn:", round(time()-t0, 3), "s"
from sklearn.metrics import accuracy_score
acc_knn = accuracy_score(labels_test, pred_knn)
print "accuracy knn:", acc_knn

print "Random Forest"
from sklearn.ensemble import RandomForestClassifier
clf_rf = RandomForestClassifier(n_estimators=100, criterion="gini", min_samples_split=100)
t0 = time()
clf_rf.fit(features_train, labels_train)
print "training time rf:", round(time()-t0, 3), "s"
t0 = time()
pred_rf = clf_rf.predict(features_test)
print "predict time rf:", round(time()-t0, 3), "s"
from sklearn.metrics import accuracy_score
acc_rf = accuracy_score(labels_test, pred_rf)
print "accuracy rf:", acc_rf

print "AdaBoost"
from sklearn.ensemble import AdaBoostClassifier
clf_ab = AdaBoostClassifier(n_estimators=50)
t0 = time()
clf_ab.fit(features_train, labels_train)
print "training time ab:", round(time()-t0, 3), "s"
t0 = time()
pred_ab = clf_ab.predict(features_test)
print "predict time ab:", round(time()-t0, 3), "s"
from sklearn.metrics import accuracy_score
acc_ab = accuracy_score(labels_test, pred_ab)
print "accuracy ab:", acc_ab

try:
    prettyPicture(clf_knn, features_test, labels_test, "img_knn.png")
    prettyPicture(clf_rf, features_test, labels_test, "img_rf.png")
    prettyPicture(clf_ab, features_test, labels_test, "img_ab.png")
except NameError:
    pass
