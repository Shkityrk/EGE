a=[int(x) for x in open("17/17var15.txt")]
l=[]
for i in range(1,len(a)):
    if a[i-1]>700 or a[i]>700:l.append(a[i-1]**2+a[i]**2)
print(len(l), max(l))