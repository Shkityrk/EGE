m=0

for i in range(248015, 251575+1):
    if i%2!=0:
        k=set()
        for d in range(1,int(i**0.5)+1):
            if i%d==0:
                k.add(d)
                k.add(i//d)
        if len(k)%2!=0:
            m+=1
            print(m,i,len(k),int(i**0.5))
