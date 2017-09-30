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
import pprint

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
poi_names = open("../final_project/poi_names.txt").readlines()

print "number of people:", len(enron_data.keys())
print "names of people:", pprint.pformat(enron_data.keys())
print "number of features:", len(enron_data['DONAHUE JR JEFFREY M'].keys())
print "names of features:", enron_data['DONAHUE JR JEFFREY M'].keys()
print "number of persons of interest:", len(
    [enron_data[key]["poi"] for key in enron_data.keys() if enron_data[key]["poi"]])
print "names of persons of interest:", [key for key in enron_data.keys() if enron_data[key]["poi"]]
print "number of persons of interest from file:", len(poi_names)
print "names of persons of interest from file:", poi_names
print "total value of the stock belonging to James Prentice:", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "email messages do we have from Wesley Colwell to persons of interest:", enron_data["COLWELL WESLEY"][
    "from_this_person_to_poi"]
print "value of stock options exercised by Jeffrey K Skilling:", enron_data["SKILLING JEFFREY K"][
    "exercised_stock_options"]
payments_list = [[key, enron_data[key]["total_payments"]] for key in enron_data.keys() if
                 key in ["LAY KENNETH L", "SKILLING JEFFREY K", "FASTOW ANDREW S"]]
# print payments_list
print "total payments:", sorted(payments_list, key=lambda x: x[1])[::-1]
print "salary list:", [[key, enron_data[key]["salary"]] for key in enron_data.keys() if
                       enron_data[key]["salary"] != "NaN"]
print "number of people with quantified salary:", len([[key, enron_data[key]["salary"]] for key in enron_data.keys() if
                                                       enron_data[key]["salary"] != "NaN"])
print "number of people with quantified email_address:", len(
    [[key, enron_data[key]["email_address"]] for key in enron_data.keys() if
     enron_data[key]["email_address"] != "NaN"])

print "percent of people having total_payments missing:", (len([enron_data[key]["total_payments"] for key in enron_data.keys() if
                                                     enron_data[key]["total_payments"] == "NaN"]) / float(len(
    enron_data.keys()))) * 100

print [enron_data[key]["poi"] for key in enron_data.keys() if enron_data[key]["total_payments"] == "NaN"]

print "people having total_payments missing:", len([enron_data[key]["total_payments"] for key in enron_data.keys() if
                                                     enron_data[key]["total_payments"] == "NaN"])
