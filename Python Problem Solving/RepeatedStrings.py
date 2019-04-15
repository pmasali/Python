s='aba'
n=10
count = s.count('a') * (n//len(s)) + s[:n%len(s)].count('a')
print(count)