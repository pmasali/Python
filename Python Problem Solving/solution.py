with open("/Users/prateekmasali/Desktop/data.txt", "r") as ins:
    array = []
    for line in ins:
        line = line.strip()
        array.append(line.split(','))

final = []
flag = []
for i, record in enumerate(array):
    if i not in flag:
        for j, entry in enumerate(array):
            if array[j][0] == record[0] and array[j][1] == record[1] and j != i:
                buffer = array[j][0],array[j][1],array[j][2]+','+array[i][2]
                final.append(buffer)
                flag.append(j)

print(final)


    # print(array[0][0])





# lines = [line.rstrip('\n') for line in open('/Users/prateekmasali/Desktop/data.txt')]
# # print(lines)
# array = []
# for record in lines:
#     array.append(record.split(','))
# print(array)
# for record in array:


# import pandas as pd
# from collections import namedtuple

# Item = namedtuple('Patient', 'AdminDate','Drug')
# items = []

# df = pd.read_csv('/Users/prateekmasali/Desktop/data.txt', sep=",", names=['Patient', 'AdminDate','Drug'])

# print(df)