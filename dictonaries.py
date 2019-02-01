#study of dictionary 
# accepting valid dictionary values
# Error out for invalid entry
# display counts

cnt = dict()
cnt['swen'] = 0
cnt['when'] = 0
cnt['den'] = 0
cnt['pen'] = 0

while True:
    value = input("enter swen/when/den/pen or end: ")
    if value == 'end': break
    if value not in cnt:
        print('invalid entry')
        #break
    else:
        cnt[value] = cnt[value] +1
print(cnt)
    
# read a file and get counts of all the distinct words

lst = list()
# /Users/prateekmasali/Desktop/Git/Python/romeo.txt
xfile = input("Enter the file: ")
fh = open(xfile)

counts = dict()
for line in fh:
    lst = line.split()
    for word in lst:
        counts[word] = counts.get(word,0) + 1

print('Counts',counts)

bigcount = 0
bigword = 0
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print('Most used word is "',bigword,'" used ',bigcount,'times')



#Assignment 9.4:

lst = list()
# /Users/prateekmasali/Desktop/Git/Python/mbox-short.txt
xfile = input("Enter the file: ")
fh = open(xfile)

counts = dict()
for line in fh:
    if line.startswith('From '):
        lst = line.split()
        word = lst[1]
        counts[word] = counts.get(word,0) + 1

print('Counts',counts)

# Gets most frequently used word
bigcount = 0
bigword = 0
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword,bigcount)

######TUPLES#######
#Gets 10 most frequently used words

ls = list()
for k,v in counts.items():
    newtup = (v,k)
    
    ls.append(newtup)
    

ls = sorted(ls,reverse = True)

for val, key in ls[:10]:
    print(key,val)

print('Sort in one line:')

print(sorted([(v,k) for k,v in counts.items()],reverse = True))


#Assignment 10.2

name = input("Enter file: ")
if len(name) < 1 : name = "/Users/prateekmasali/Desktop/Git/Python/mbox-short.txt"

handle = open(name)
lst = list()
hr = dict()
for line in handle:
    if line.startswith("From "):
        lst = line.split()
        lst = lst[5].split(':')
        a = lst[0]
        hr[str(a)] = hr.get(str(a),0) + 1

fls = list()
for k,v in hr.items():
    newtp = (k,v)
    fls.append(newtp)

fls = sorted(fls)
for k,v in fls:
    print(k,v)