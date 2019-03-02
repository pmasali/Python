ar = [10,20,20,10,10,30,50,10,20]
n = 9
ar = sorted(ar)
print(ar)
index = 0
pair = 0
while index < n-1:
    if ar[index] == ar[index+1]:
        pair += 1
        index += 2
    else:
        index += 1
print(pair)

