#!/usr/bin/python


def outlierCleaner(predictions, ages_train, net_worths_train):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cd = []
    diff = []
    for i in range(0, len(predictions)):
        diff.append(abs(predictions[i] - net_worths_train[i]))
        cd.append((ages_train[i], net_worths_train[i], diff[i]))

    cd = sorted(cd, key=lambda x: x[2])
    return cd[:int(0.9*len(cd))]
