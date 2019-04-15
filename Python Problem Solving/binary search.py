## BINARY SEARCH:
# # nailing planks solution:
# def solution(A, B, C):
#     # write your code in Python 3.6
#     min_plank = 0
#     max_plank = len(A)-1
#     plank = [0]*len(A)
#     for index,nail in enumerate(C):
#         min_plank = 0
#         max_plank = len(A)-1
#         while (min_plank <= max_plank):
#             if nail >= A[min_plank] and nail <= B[min_plank]:
#                 plank[min_plank] = 1
#                 min_plank += 1
#                 if set(plank) == {1}:
#                     return index+1
#             else:
#                 min_plank += 1
#     if set(plank) != {1}:
#         return -1
      
#     pass

# solution([1, 4, 5, 8], [4, 5, 9, 10], [4, 6, 7, 10, 2])

# C = [4, 6, 7, 10, 2]
# nails = sorted(enumerate(C), key = lambda x: x[1])
# print(nails)
# print(len(nails))

# print(sum(C[0:1]))


# def solution(A):
#     # write your code in Python 3.6
#     if len(A) < 3:
#         return abs(A[0]-A[1])
#     P = 1
#     t1 = 0
#     t2 = 0
#     min = abs(sum(A))
#     while (P < len(A)):
#         t1 = sum(A[0:P])
#         t2 = sum(A[P:len(A)])
#         if (abs(t1-t2)<min):
#             min = abs(t1-t2)
#         P += 1
#     return min       
#     pass

# A = [-2, -3, -4, -1]
# print(solution(A))

# def solution(A):
#     # write your code in Python 3.6
#     A.sort()
#     print(A)
#     if A[len(A)-1] == len(A):
#         return 1
#     else:
#         return 0
#     pass

# A = [4, 1, 3, 2]
# print(solution(A))
import re
def solution(A):
    A = A.replace("-","")
    A = A.replace(" ","")
    final = ''
    flag = 0
    if len(A)%3 == 0:
        for index, n in enumerate(A):
            if index == 0:
                final += n
            elif index%3 == 0:
                final += '-'
                final += n
            else:
                final += n
    if len(A)%3 == 1:
        for index, n in enumerate(A):
            if index%3 == 1:
                if flag != 1:
                    final += '-'
                    flag = 0
                final += n
            else:
                if len(A)-index == 4:
                    flag = 1
                final += n
    if len(A)%3 == 2:
        for index, n in enumerate(A):
            final += n
    return final
    
    
            
    # return A

print(solution("222-22 2  22---22222"))