f=open('kompege/17_1993.txt')
a=[int(x) for x in f.readlines()]
ans=[]

for i in range(len(a)-1):
    s=a[i-1]+a[i]
    if s%3==0 and s%6!=0 and abs(a[i]*a[i-1])%10==8:ans.append(s)
print(len(ans), max(ans))