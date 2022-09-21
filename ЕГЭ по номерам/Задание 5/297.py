for n in range(1000000000000000,2000000000000000):
    s=str(n)
    summ=0
    summ1=0
    for i in range(len(s)):
        if i%2!=0:
            summ+=int(s[i])
        else:
            l=int(s[i])
            if l*2<10: summ1+=l*2
            else: summ1+= ((l*2)//10)+((l*2)%10)
    if summ+summ1==30:
        print(n)
        break
        
