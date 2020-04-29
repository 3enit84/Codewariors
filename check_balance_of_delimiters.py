S = input()

if (len(S) % 2) == 0: #even number
    bl=br=cl=cr=sl=sr=0
    for s in S:
        if s=='(':
            bl += 1#brecket left
        if s==')':
            br += 1#brecket right
        if s=='{':
            cl += 1#curly left
        if s=='}':
            cr += 1#curly right
        if s=='[':
            sl += 1#square left
        if s==']':
            sr += 1#square right
    if bl==br and cl==cr and sl==sr:
        print('True')
    else: print('False')            
else: print('False')
