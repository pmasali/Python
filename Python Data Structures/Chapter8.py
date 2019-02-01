#Lists
#1:simple difference
friends = ['joe','moe','poe']

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year: ',friend)

for friend in friends:
    print('Happy New Year: ',friend)

#2: cal average
numlist = list()
while True:
    inp = input("enter a number:")
    if inp == "done" : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average of numbers: ', average)

#3: strings in list
text = 'my name is prateek masali ,'
txt = text.split()
print(txt)

#4: arrange list

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])

#5: find a pattern (working with dataset)

xfile = open('/Users/prateekmasali/Desktop/Git/Python/mbox-short.txt')
words = list()
for line in xfile:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    # print(line)
    words.append(line.split())
#Getting Distinct days for email was sent
days = list()
for i in words:
    if i[2] in days: continue
    days.append(i[2])
print(days)

#6: 8.4 assignment
# /Users/prateekmasali/Desktop/Git/Python/romeo.txt
xfile = input("Enter the file:")
fh = open(xfile)
lst = list()
buffer = list()
for line in fh:
    buffer = line.split()
    for x in buffer:
        if x not in lst :
            lst.append(x)
lst.sort()
print(lst)

#7: 8.5 Assignment
# /Users/prateekmasali/Desktop/Git/Python/mbox-short.txt
xfile = input("Enter the file:")
fh = open(xfile)
count = 0
words = list()
for line in fh:
    line = line.rstrip()
    if not line.startswith('From:'): continue
    words = line.split()
    print(words[1])
    count += 1
print("There were", count, "lines in the file with From as the first word")
