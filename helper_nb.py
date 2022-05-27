#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np

import pickle
def run_model(userx):
    print(userx)



    with open('model.p', 'rb') as file:
        model = pickle.load(file)

    with open('mushrooms.p', 'rb') as file:
        mushrooms = pickle.load(file)

    mushrooms_new = mushrooms.copy()

    # i only wnat the columns' names now
    mushrooms_new = mushrooms_new.iloc[0:0]

    list_of_unique = []
    for col in mushrooms:
        list_of_unique.append(list(mushrooms[col].unique()))


    n_rows = 12


    for i in range(n_rows):
        # print(i)
        temp_list = []
        for col in list_of_unique:
            if (len(col) > i):
                # print(col[i])
                temp_list.append(col[i])
            else:
                # print(col[0])
                temp_list.append(col[0])
        mushrooms_new.loc[i] = temp_list

    # drop class from this df
    mushrooms_new = mushrooms_new.drop(columns=['class'])

    # start function here


    mushrooms_new.loc[12] = userx


# # column class: 0 -> poisonous, 1 -> edible

# # f - false, t - true
    mushrooms_new['bruises'] = mushrooms_new['bruises'].replace({'f':0, 't':1})

# # a - attached, f-free
    mushrooms_new['gill-attachment'] = mushrooms_new['gill-attachment'].replace({'f':0, 'a':1})

# # c - close, w - crowded
    mushrooms_new['gill-spacing'] = mushrooms_new['gill-spacing'].replace({'c':0, 'w':1})


    mushrooms_new['gill-size'] = mushrooms_new['gill-size'].replace({'n':0, 'b':1})

    mushrooms_new['stalk-shape'] = mushrooms_new['stalk-shape'].replace({'t':0, 'e':1})

    many_labels = ['cap-shape', 'cap-surface', 'cap-color', 'odor', 'gill-color', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat']


    mushrooms_new = mushrooms_new.drop(columns=['veil-type'])


    mushrooms_new = pd.get_dummies(mushrooms_new, columns= many_labels)

    print(mushrooms_new.shape)
    sol = model.predict(mushrooms_new)
    sol = sol[-1]
    print(sol)
    return sol
#userx = ['b', 'f', 'n', 't', 'a', 'a', 'c', 'b', 'k', 'e', 'b', 'f', 'y', 'n', 'b', 'p', 'o', 'o', 'e', 'n', 'c', 'l']
#run_model(userx)



