f=open('kompege/17_2003.txt')
a=[int(x) for x in f.readlines()]
ans=[]
l=0
for i in range(len(a)):
    if a[i]%3==0 and a[i]%7!=0 and a[i]%17!=0\
            and a[i]%19!=0 and a[i]%27!=0:
        ans.append(a[i])
print(len(ans), max(ans))
