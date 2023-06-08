f=open('kompege/17_2402.txt')
a=[int(x) for x in f.readlines()]
ans=[]

for i in range(2,len(a)):
    if a[i-2]%3==2 or a[i-1]%3==2 or a[i]%3==2:
        ans.append(min(a[i-2],a[i-1],a[i]))
print(len(ans), sum(ans))