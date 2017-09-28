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
poi_names = open("../final_project/poi_names.txt").readlines()

print "number of people:", len(enron_data.keys())
print "names of people:", enron_data.keys()
print "number of features:", len(enron_data['DONAHUE JR JEFFREY M'].keys())
print "names of features:", enron_data['DONAHUE JR JEFFREY M'].keys()
print "number of persons of interest:", len([enron_data[key]["poi"] for key in enron_data.keys() if enron_data[key]["poi"]])
print "names of persons of interest:", [key for key in enron_data.keys() if enron_data[key]["poi"]]
print "number of persons of interest from file:", len(poi_names)
print "names of persons of interest from file:", poi_names
print "total value of the stock belonging to James Prentice:", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "email messages do we have from Wesley Colwell to persons of interest:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "value of stock options exercised by Jeffrey K Skilling:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]