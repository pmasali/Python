# Using map function
# Extract Title and Last Name
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

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
def TimesFunction():
    lst = []
    for i in range(10):
        for j in range(10):
            lst.append(i*j)
    return lst

print(TimesFunction())

print([i*j for i in range(10) for j in range(10)])