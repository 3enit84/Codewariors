F = input()

rec = str.split(F,',')
Lst = []
for r in rec:
    Lst += [int(r)]
Lst.sort()
for i in range(0,len(Lst),2):
    try:
        if Lst[i]!=Lst[i+1]:
            print(Lst[i])
            break
    except IndexError: print(Lst[-1])
