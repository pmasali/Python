# def solution(A):
#     result = 0
#     b = list(set([a for a in A if a > 0]))
#     print(b)
#     if min(b, default = 0) > 1 or min(b, default = 0) == 0:
#         result = 1
#     else:
#         for i,a in enumerate(b):
#             if (a - b[i-1]) > 1:
#                 result = b[i-1]+1
#                 return result
#             if i == len(b)-1:
#                 result = b[-1]+1
    
#     return result

def solution(A):
    ans = 0
    for i in range(0, len(A)):
        if A[i] < ans:
            print(i)
            ans = A[i]
    return ans

A = [-1, 1, -2, 2]
print(solution(A))