text = "X-DSPAM-Confidence:    0.8475"
a = int(text.find(':'))
b = int(len(text))
c = float(text[a+1:b])
print(c)


fruit = 'banana'
if 'n' in fruit :
    print("found n in " + fruit)
if 'm' not in fruit :
    print("not found m in " + fruit)

caps = fruit.capitalize()#upper, lower, 
print(caps)

greet = ('Hello Bob. Bob is a friend')
greet1 = greet.replace('bob','adam') #case sensitive
print(greet1)
greet2 = greet.replace('Bob','adam')
print(greet2)

info = '      Space on left removed using lstrip'
print(info)
info1 = info.lstrip()#rstrip on right. strip on both sides.
print(info1)

greet.startswith('Hello') # returns true of false

