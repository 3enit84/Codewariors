F = int(input())

Lst = [0]
for i in range(F): #make Fabinacci list
    Lst += [1]
for j in range(3,len(Lst)):
    Lst[j] = Lst[j-1]+Lst[j-2]
#print(Lst)
#print(len(Lst))
print(Lst[-1])
