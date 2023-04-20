f=open('files/27-102b.txt')
n=int(f.readline())
k=0
m=524288

a=[int(x) for x in f.readlines()]

for x in range(len(a)):
    p=0
    if a[x]%m!=0:
        k+=1
        p=a[x]
        for y in range(x+1,len(a)):
            p*=a[y]
            if p%m!=0 and p!=0:
                k+=1
            else:break
print(k)