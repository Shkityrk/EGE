a=[int(x) for x in open("17/17var13.txt")]
l=[]
for i in range(1,len(a)):
    if a[i]+a[i-1]>=100 and ((a[i-1]<0) or (a[i]<0)):l.append(a[i]*a[i-1])
print(len(l), max(l))