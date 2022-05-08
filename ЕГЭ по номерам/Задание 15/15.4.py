def d (n,m):
    return n%m
for a in range (1, 10000):
    flag=0
    for x in range (1, 1000):
        for y in range (1, 1000):
            if (d(144,a) and (( not d(x,a) and d(x,66)) <= (not d(x, 105))) )==0:
                flag =1
                break
        if flag ==1:
            break
    if flag==0:
        print (a)