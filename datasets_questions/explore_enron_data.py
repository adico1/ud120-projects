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

<<<<<<< HEAD
# load the dataset
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print "All Data"
print enron_data

# How many people are in the dataset?
print "How many people are in the dataset?"
print len(enron_data.keys())

# How many features in the dataset
print "How many features in the dataset"
print len(enron_data[enron_data.keys()[0]].keys())

# How many POIs are there in the E+F dataset?
print "How many POIs are there in the E+F dataset?"
print sum(1 for x in enron_data.values() if x['poi']==1)

# What is the total value of the stock belonging to James Prentice?
print "What is the total value of the stock belonging to James Prentice?"
print enron_data["PRENTICE JAMES"]["total_stock_value"]

# How many email messages do we have from Wesley Colwell to persons of interest?
print "How many email messages do we have from Wesley Colwell to persons of interest?"
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# What's the value of stock options exercised by Jeffrey K Skilling?
print "What's the value of stock options exercised by Jeffrey K Skilling?"
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# How much money did that person get?
print "How much money did that person get?"
print "Skilling, Jeffrey"
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Fastow, Andrew"
print enron_data["FASTOW ANDREW S"]["total_payments"]
print "Lay, Kenneth"
print enron_data["LAY KENNETH L"]["total_payments"]

# How many folks in this dataset have a quantified salary? What about a known email address?

