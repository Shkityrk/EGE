f=open('data/26-45.txt')
a=[int(x) for x in f.readlines()]
le=a[0]
a=a[1:]
b=a
s=[]

for i in range(le-1):
    for j in range(i+1,le):
        if i!=j and a[i]!=0 and a[j]!=0:
            sr=(a[i]+a[j])
            if sr%2==0:
                for x in b:
                    if sr//2==x:
                        s.append(sr)
                        print(i,a[i], a[j], sr)
                        break

    a[i] = 0

print(len(s),max(s))