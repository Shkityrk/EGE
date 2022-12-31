a=[int(x) for x in open("data/17-339.txt")]
l=[]
mn=0
mn = min(x for x in a if x%19==0 and x>0)
print(mn)

for i in range(1,len(a)):
    if a[i]+a[i-1]<mn: l.append(a[i]+a[i-1])
print(len(l), max(l))
