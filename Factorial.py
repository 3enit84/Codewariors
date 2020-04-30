F = int(input())

Lst = []
for i in range(1,F+1):
    Lst += [i]
Prod = 1#product
for f in range(len(Lst)):
    Prod = Prod*Lst[f]
print(Prod)
