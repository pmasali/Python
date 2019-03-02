# def solution(X, Y, D):
#     # write your code in Python 3.6
#     count = (Y-X)//D
#     return (count+1)

# print(solution(10,85,30))

# count = 85-10
# count = count // 30
# print(count+1)

# Write a function:

# def solution(A, K)

# that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

# For example, given

#     A = [3, 8, 9, 7, 6]
#     K = 3
# the function should return [9, 7, 6, 3, 8]. Three rotations were made:

#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
# For another example, given

#     A = [0, 0, 0]
#     K = 1
# the function should return [0, 0, 0] 


# # # rotate list to the given number of times
# def solution(A, K):
#     # write your code in Python 3.6
#     if len(set(A)) <= 1:
#         return A
#     else:
#         i = 0
#         b = []
#         while (i <= len(A)-1):
#             if (K < 1):
#                 K = len(A)
#             b.append(A[(len(A)-K)])
#             K -= 1
#             i += 1
#         return b

# print(solution([3,8],3))

# def solution(A):
#     # write your code in Python 3.6
#     A.sort()
#     if len(A) == 1 and A[0] != 1:
#         return 1
#     if len(A) > 1 and A[0] != 1:
#         return 1
#     for index,value in enumerate(A):
#         if (index < len(A)-1) and ((A[index+1]-value) > 1):
#             return value+1
#         elif index == len(A)-1:
#                 return value + 1
            
#     pass

# print(solution([2,3,4,1,5]))