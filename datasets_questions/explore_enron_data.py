#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "number of people:", len(enron_data.keys())
print "number of features:", len(enron_data['DONAHUE JR JEFFREY M'].keys())
print "number of poi:", len([enron_data[key]["poi"] for key in enron_data.keys() if enron_data[key]["poi"]])
print "names of poi:", [key for key in enron_data.keys() if enron_data[key]["poi"]]
