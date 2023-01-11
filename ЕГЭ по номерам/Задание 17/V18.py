a=[int(x) for x in open("17/17var18.txt")]
l=[]
for i in range(1,len(a)):
    if a[i-1]< 310 and a[i]<310:l.append(a[i-1]**3+a[i]**3)
print(len(l), min(l))