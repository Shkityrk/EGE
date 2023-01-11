a=[int(x) for x in open("17/17var16.txt")]
l=[]

for i in range(1,len(a)):
    if a[i]>300 or a[i-1]>300: l.append(a[i]**2+a[i-1]**2)
print(len(l), min(l))