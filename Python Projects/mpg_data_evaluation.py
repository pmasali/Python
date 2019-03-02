# # Importing mpg.csv file
# import csv

# with open('/Users/prateekmasali/Desktop/Git/Python/mpg.csv') as csvfile:
#     mpg = list(csv.DictReader(csvfile))
# # understanding the data
# print(mpg[:3])
# print(len(mpg))
# print(mpg[0].keys())
# avg_mpg_city = sum(float(d['cty']) for d in mpg) / len(mpg)
# print(round(avg_mpg_city,2))
# #################################################
# # Calculation my cylinders
# cylinders = set(d['cyl'] for d in mpg)
# print(cylinders)

# ctympgbycyl = []
# for c in cylinders:
#     citympgtmp = 0
#     countmpgtmp = 0
#     for d in mpg:
#         if d['cyl'] == c:
#             citympgtmp += float(d['cty'])
#             countmpgtmp += 1
#     ctympgbycyl.append((c, round(citympgtmp / countmpgtmp,2)))

# ctympgbycyl.sort(key=lambda x: x[0])
# print(ctympgbycyl)

# #################################################
# # Calculation my Vehicle type

# vehicleType = set(d['class'] for d in mpg)
# print(vehicleType)

# HwyMpgByClass = []
# for a in vehicleType:
#     sumHwyMpg = 0
#     countHwyMpg = 0
#     for b in mpg:
#         if b['class'] == a:
#             sumHwyMpg += float(b['hwy'])
#             countHwyMpg += 1
#     HwyMpgByClass.append((a, round(sumHwyMpg / countHwyMpg,1)))

# HwyMpgByClass.sort(key = lambda x: x[1])
# print(HwyMpgByClass)

#################################################
# Date time understanding

import datetime as dt
import time as tm

print(tm.time())

dtnow = dt.datetime.fromtimestamp(tm.time())
print(dtnow)

print(dtnow.year, dtnow.month, dtnow.day)

dlta = dt.timedelta(days = 100)
print(dlta)

today = dt.datetime.today()
print(today)

print(today-dlta)