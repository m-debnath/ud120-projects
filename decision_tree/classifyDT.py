from sklearn import tree


def classify(features_train, labels_train):
    clf = tree.DecisionTreeClassifier(min_samples_split=2)
    clf.fit(features_train, labels_train)
    return clf

