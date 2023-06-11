f=open('files_kompege/26_936.txt')
n,s=map(int, f.readline().split())
a=[int(x) for x in f]
a.sort(reverse=1)

count=0
last=0

s1=0
while len(a)>0:
    for i in range(len(a)):
        if s1+a[i]<=s:
            s1+=a[i]
            a[i]=0
    a=[x for x in a if x!=0]
    count+=1
    last=s1
    s1=0
print(count,last)