
for x in range(1,100,1):
    Sum = 0
    N=0
    a = 36 ** 17 - 6 ** x + 71
    while a !=0:
        N=a%6
        Sum=Sum+N
        a=a//6
print (Sum)