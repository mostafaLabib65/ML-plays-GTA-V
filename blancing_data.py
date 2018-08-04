import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle


training_data = np.load('training_data-5-balanced.npy')


df = pd.DataFrame(training_data)
print(df.head())
print(len(training_data))
print(Counter(df[1].apply(str)))
'''
lefts = []
rights = []
forwords = []

shuffle(training_data)

for data in training_data:
    screen = data[0]
    choise = data[1]
    if choise == [1, 0, 0]:
        lefts.append([screen, choise])
    elif choise == [0, 1, 0]:
        forwords.append([screen, choise])
    elif choise == [0, 0, 1]:
        rights.append([screen, choise])

forwords =forwords[:len(lefts)][:len(rights)]
lefts = lefts[:len(forwords)]
rights = lefts[:len(forwords)]

finalData = forwords + lefts + rights
shuffle(finalData)

np.save('training_data_v2.npy')
'''