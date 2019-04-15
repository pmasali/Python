# def isStringInArray(a1, a2):
#     i = len(a1)
#     j = len(a2)
#     m = 0
#     n = 0

#     while (m<i and n<j):
#         if (a1[m] == a2[n]):
#             m = m + 1
#         n = n + 1
#     if (m == i):
#         return "present"
#     else:
#         return "not present"

# print(isStringInArray("cam","cancun"))

# def chk_palindrome(A):
#     i = 0
#     j = len(A)-1
#     if len(A) == 1:
#         return "palindrome"
#     while i<j and A[i]==A[j]:
#         i += 1
#         j -= 1
#     if i>j or i==j:
#         return "palindrome"
#     else:
#         return "not palindrome"

# print(chk_palindrome("a"))

def cleanPhone(N):
    N = N.replace("-","")
    N = N.replace(" ","")
    final = ""
    if len(N)%10 == 0:
        final = N[0:3]+"-"+N[3:6]+"-"+N[6:]
    elif len(N) > 10:
        final = N[0:3]+"-"+N[3:6]+"-"+N[6:8]+"-"+N[8:]
    elif len(N) < 10:
        final = N[0:3]+"-"+N[3:6]+"-"+N[6:]
    return final


print(cleanPhone("123-456---78   "))
