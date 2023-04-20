f=open('data/26-45.txt')
a=[int(x) for x in f.readlines()]
le=a[0]
a=a[1:]
b=a
s=[]

for i in range(le-1):
    for j in range(i+1,le):
        if i!=j and a[i]!=0 and a[j]!=0:
            sr=(a[i]+a[j])//2
            for x in b:
                if int(sr)==x:
                    s.append(sr)
                    print(i,a[i], a[j], sr)
                    a[i]=0
                    a[j]=0
                    break


print(len(s),max(s))