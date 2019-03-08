# with open("/Users/prateekmasali/Desktop/data.txt", "r") as ins:
#     array = []
#     for line in ins:
#         array.append(rstrip(line))
    
# lines = [line.rstrip('\n') for line in open('/Users/prateekmasali/Desktop/data.txt')]
# # print(lines)
# array = []
# for record in lines:
#     array.append(record.split(','))
# print(array)
# for record in array:


import pandas as pd
from collections import namedtuple

Item = namedtuple('Patient', 'AdminDate','Drug')
items = []

df = pd.read_csv('/Users/prateekmasali/Desktop/data.txt', sep=",", names=['Patient', 'AdminDate','Drug'])

print(df)