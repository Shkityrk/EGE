f=open('kompege/17_2002.txt')
a=[int(x) for x in f.readlines()]
ans=[]

for i in range(3,len(a)):
    if a[i-3]>a[i-2]>a[i-1]>a[i] and a[i-3]-a[i]>1000:
        ans