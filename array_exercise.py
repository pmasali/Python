# from collections import Counter

def checkMagazine(magazine, rasom):
    return (Counter(rasom) - Counter(magazine)) == {}

# if __name__ == '__main__':
#     mn = input().split()
#     m = int(mn[0])
#     n = int(mn[1])
#     magazine = input().rstrip().split()
#     note = input().rstrip().split()
#     if checkMagazine(magazine, note) == {}:
#         print ('note complete')
#     else:
#         print ('note not complete')


# I am the king no one can rule me This is my place and this can not change
# I am king this place can change no rule
# L = [-1]+A
# print(L)
# n=len(A)
# pos=(n+1)//2
# print(pos)

##################################
# A = [0,100,150,200,201]
# A = [-1,-2,-5,-7,-1,-2]
# A = [0]
    
def missingVal(A):
    A.sort()
    if A[len(A)-1] < 0:
        return 1
        #-3,-1,0,3
    else:
        for index,val in enumerate(A):
            if ((index == len(A)-1) and (A[len(A)-1] >= 0)) or ((index < (len(A)-1)) and (A[index+1]-A[index] > 1)):
                return val + 1

# print(missingVal([-3,-2,-1]))

#########################################
#0,1,1,2,3,5,8,13,21,34
def fiboNum(num):
    A = [0,1]
    i=0
    while i < num-2:
        A.append(A[i]+A[i+1])
        i += 1
    return A

# print(fiboNum(1))
