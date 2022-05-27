#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 12:48:38 2021

@author: ironhack
"""

import pickle

def pre_run(input_list):
    print(input_list)
    return



def run_model(mylist):
    
    X_new = [mylist]
    
    #load the model from the pickle
    with open('model.p', 'rb') as file:
        pickle_model = pickle.load(file)
        
    prediction = pickle_model.predict(X_new)
    
    return prediction

