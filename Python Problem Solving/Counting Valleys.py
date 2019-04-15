# n = 8
# s = 'UDDDUDUU'
# stp = 0
# level = 0
# valley = 0
# while stp < n:
#     for i in s:
#         if i == 'U':
#             level += 1
#             if level == 0: valley += 1
#         if i == 'D':
#             level -= 1
#         stp += 1
# print(valley)


def solution(A):
    CastleCount = 0
    index = 0
    first = 0
    while index < (len(A)):
        if index < len(A)-1 and A[index] == A[index+1]:
            index += 1
        elif index == len(A)-1 and A[index] != A[index-1]:
            CastleCount += 1
            index += 1
        elif A[index+1] != A[index] and first == 0:
            CastleCount += 1
            first = 1
            index += 1
        elif len(A) > 2 and index != 0 and index != len(A)-1 and A[index-1] < A[index] > A[index+1]:
            CastleCount += 1
            index += 1
        elif len(A) > 2 and index != 0 and index != len(A)-1 and A[index-1] > A[index] < A[index+1]:
            CastleCount += 1
            index += 1
        else:
            index += 1
            continue
    return CastleCount

A = [1,1,2,3,5,2,1,2,6,7]
print(solution(A))