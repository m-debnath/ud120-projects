import sys
sys.path.append("../choose_your_own/")
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import copy
import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()


########################## SVM #################################
### we handle the import statement and SVC creation for you here
from sklearn.svm import SVC
# from sklearn.naive_bayes import GaussianNB
# clf = SVC(C=1.0, kernel="linear", gamma=1.0)
# clf = SVC(C=1.0, kernel="poly", gamma=1.0)
clf = SVC(C=1000.0, kernel="rbf", gamma=1.0) # accuracy: 0.94
# clf = SVC(C=1.0, kernel="sigmoid", gamma=1.0)
# clf = GaussianNB() # accuracy: 0.884

#### now your job is to fit the classifier
#### using the training features/labels, and to
#### make a set of predictions on the test data
clf.fit(features_train, labels_train)


#### store your predictions in a list named pred
pred = clf.predict(features_test)

prettyPicture(clf, features_test, labels_test)
plt.show()


from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, pred)
print "accuracy:", acc

