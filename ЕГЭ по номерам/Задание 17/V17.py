a=[int(x) for x in open("17/17var17.txt")]
l=[]
for i in range(1,len(a)):
    if a[i-1]<450 and a[i]<450:l.append(a[i-1]**3+a[i]**3)
print(len(l), max(l))