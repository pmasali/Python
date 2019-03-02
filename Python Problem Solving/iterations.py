## report unpaired elements
## A = [9,3,9,3,9,7]

# def solution(A):
#     B = []
#     for i in A:
#         if (A.count(i) % 2) > 0 and (i not in B):
#             B.append(i)
#     return B
# print(solution([9,3,9,3,9,7]))

## Binary Gap between two 1's
# def solution(N):
#     B = bin(N)[2:]
#     i = 0
#     j = 1
#     highest = 0
#     count = 0
#     while (i < len(B)) and (j < len(B)):
#         if (B[j] == '0') and (j < len(B)):
#             count += 1
#             j = j + 1
#         else:
#             i = j
#             j = j + 1
#             if (count > highest):
#                 highest = count
#             count = 0
        
#     return highest

# print(solution(1000))
        

## detecting if given string is a palindrome

def solution(word):
    if len(word) == 1:
        print('it is a palindrome')
    i = 0
    j = len(word)-1
    while (i < j) and (word[i] == word[j]):
        i += 1
        j -= 1
        if (i == j) or (i > j):
            print('it is a palindrome')
    if (word[i] != word[j]):
        print('it is not a palindrome')
solution('a')
        