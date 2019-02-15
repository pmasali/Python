# for num in range(0,100):
#     if num % 15 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

str = "create a list of first letter of every word"
lst = list()
lst = ([word[0] for word in str.split()])
print(lst)

for wrd in str.split():
    if wrd[0].lower() == 'l':
        print(wrd)