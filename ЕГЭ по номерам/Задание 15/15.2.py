for a in range(1,1000):
    flag=0
    for x in range(0,1000):
        if (( ((x&a==0) or (x&13!=0))<= (x&13!=0)) or ( x&a!=0) or (x&39==0))==0:
            flag=1
            break
    if flag==0:
        print(a)
        break
