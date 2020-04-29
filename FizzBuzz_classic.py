I = int(input())

for i in range(1,I+1):
    #print(i)
    if (i % 3)==0 and (i % 5)==0:
        print('FizzBuzz')
        continue
    if (i % 3)==0:
        print('Fizz')
        continue
    if (i % 5)==0:
        print('Buzz')
    else: print(i)
