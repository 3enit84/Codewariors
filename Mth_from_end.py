M = int(input())
L = input()
rec = str.split(L,' ')
lst = []
for r in rec:
    lst += [int(r)]
#print(lst)
#print(len(lst))
def Mth_from_end(M, L):
    if M <= len(L):
        return L[len(L)-M]
    else: return "NIL"

print(Mth_from_end(M, lst))
