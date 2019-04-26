import os

inputdir = '/Users/prateekmasali/Desktop/Git/Python/Python Projects/MultiFileLoad/data/'
outputdir = '/Users/prateekmasali/Desktop/Git/Python/Python Projects/MultiFileLoad/Output/'

filelist = os.listdir(inputdir)
records = []
max = 0
for i in filelist:
    with open(inputdir+i,'r') as f:
        next(f)
        for line in f:
            fline = f.readlines()
            for record in fline:
                record = record.strip()
                records.append(record.split('\t'))
records = sorted(records,key = lambda x:int(x[0]))
# print(records)
for record in records:
    if int(record[1]) > max:
        max = int(record[1])
print('-----------------------------------------------------------------------------------------------')
print('highest score across all files:', max)
recordSum = {}
recordCount = {}
for rec in records:
    try:
        recordSum[rec[0]] = recordSum[rec[0]]+int(rec[1])
    except:
        recordSum[rec[0]] = int(rec[1])
    recordCount[rec[0]] = recordCount.get(rec[0],0) + 1
print('-----------------------------------------------------------------------------------------------')
print('Sum of all gamers:', recordSum)
print('-----------------------------------------------------------------------------------------------')
print('Count of all gamers:', recordCount)    
print('-----------------------------------------------------------------------------------------------')

recordAvg = {}

for k,v in recordSum.items():
    avg = round(recordSum[k] / recordCount[k],2)
    recordAvg[k] = avg

print('Avg of all gamers:', recordAvg)
print('-----------------------------------------------------------------------------------------------')
