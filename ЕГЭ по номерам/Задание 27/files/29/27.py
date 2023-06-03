f=open('27-29b.txt')
n=int(f.readline())
s=0
list=[]
for i in range(n):
    a=[int(x) for x in f.readline().split()]
    a=sorted(a,reverse=True)
    s+=a[0]+a[1]
    list.append(a[1]-a[2])
list=sorted(list)
if s%5!=0:
    print(s)
else:
    for i in range(len(list)):
        if s-list[i]%5!=0:
            print(s-list[i])
            break
