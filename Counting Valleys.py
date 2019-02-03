n = 8
s = 'UDDDUDUU'
stp = 0
level = 0
valley = 0
while stp < n:
    for i in s:
        if i == 'U':
            level += 1
            if level == 0: valley += 1
        if i == 'D':
            level -= 1
        stp += 1
print(valley)
