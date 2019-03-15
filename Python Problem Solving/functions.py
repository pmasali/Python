# Using map function
# Extract Title and Last Name
# people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

# def split_title_and_name(person):
#     title = person.split()[0]
#     lastname = person.split()[-1]
#     return '{} {}'.format(title, lastname)

# print(list(map(split_title_and_name, people)))

# USING LAMBDA AND MAP FUNCTIONS
# def split_title_and_name(person):
#     return person.split()[0] + ' ' + person.split()[-1]

# for person in people:
#     print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

# list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))

####################################################################################################################################################
# LIST COMPREHENSION
# def TimesFunction():
#     lst = []
#     for i in range(10):
#         for j in range(10):
#             lst.append(i*j)
#     return lst

# print(TimesFunction())

# print([i*j for i in range(10) for j in range(10)])

####################################################################################################################################################
# # Counting the group with highest number of digits, where the difference between the digits is <= 1
# a = [1,3,5,1,3,5,3,6,3,6,5,6,3]
# print(max([sum((a.count(i), a.count(i+1))) for i in set(a)]))

####################################################################################################################################################
# Drawing book
# n = 10
# p = 6
# print(min(p//2, n//2 - p//2))

####################################################################################################################################################

# function to return numbers between x & y that are evenly divisible by z

# def DivZFun(x,y,z):
#     array = []
#     for num in range(x,y):
#         if num % z == 0:
#             array.append(num)
#     return array

# print(DivZFun(1,20,2))

####################################################################################################################################################
# A=[A,B,C,D]	    B=[1,2,3,4]	C=[(4,A),(3,B),(2,C),(D,1)]    D={A:4,B:4,C:4,D:1}
# Code to produce C from A and B

A = ['A','B','C','D']	    
B = [1,2,3]

def ListCD():
    C = []
    D = {}
    # B.reverse()
    C = list(zip(reversed(B),A))
    D = dict(zip(A,reversed(B)))
    return C, D

print(ListCD())