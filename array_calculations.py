##two sum

# def add_num(A,total):
#     if (len(A) < 3) and (sum(A) == total):
#         return A
#     else:
#         i=0
#         j=1
#         while (i < len(A))and j < len(A):
#             if (A[i]+A[j]==total):
#                 return A[i], A[j]
#             else:
#                 j+=1
#             i+=1

# print(add_num([3,5],8))

# # two sum using dictionary
# def add_sum(A, total):
#     d= {}
#     for i in A:
#         d[i] = i
#     for k,v in d.items():
#         for i in A:
#             z = v + i
#             t = total - z
#             if t in d.values():
#                 return v, i, t
#     return False

# print(add_sum([1,2,3,4,5],12))

# # anagram using dictionary
# def anagram(word1,word2):
#     dict1 = {}
#     for a in word1:
#         dict1[a] = dict1.get(a,0) + 1
#     for b in word2:
#         dict1[b] = dict1.get(b,0) - 1
#         if dict1[b] < 0:
#             print('not complete')
#             break
#     else:
#         print('complete')

# anagram using list

def anagram(word1,word2):
    l1 = []
    l2 = []
    for i in word1:
        l1.append(i)
    for i in word2:
        try:
            l1.remove(i)
        except:
            print("incomplete")
            break
    if l1 == []:
        print("complete")
    # if sorted(l1) == sorted(l2):
    #     print("complete")
    # else:
    #     print("incomplete")

anagram('amit','mita')
anagram('esha','shahi')