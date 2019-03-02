xfile = '/Users/prateekmasali/Desktop/Git/Python/words.txt'
try:
    xfile = open(xfile)
except:
    print('File cannot be opened')
    quit()

#task1:
for line in xfile:
    line = line.rstrip()
    print(line.upper())

#task2:
for line in xfile:
    if 'to' in line:#line.find('From:'):
        print(line.rstrip())
    else:
        print ('1')

#task3:
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    print(line.upper())

#Task4:

fname = input("Enter file name: ")
fh = open(fname)
d = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    else:
        a = int(line.find(':'))
        b = int(len(line))
        c = float(line[a+1:b])
        d += c
        count += 1
avg = d/count
print('Average spam confidence: '+ str(avg))