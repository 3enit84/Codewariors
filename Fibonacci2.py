Flst = []

while 1:
    try:
        Flst += [int(input())]
    except EOFError: break      
#print(Flst)

for F in Flst:
    Lst = [0]
    for i in range(F): #make Fibonacci list
        Lst += [1]
    for j in range(3,len(Lst)):
        Lst[j] = Lst[j-1]+Lst[j-2]
    print(Lst[-1])
