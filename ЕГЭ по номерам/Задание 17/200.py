a=[int(x) for x in open("data/17-199.txt")]
l=[]

for i in range(2,len(a)):
    if a[i-1]>0 and len(str(a[i-1]))==2 and a[i-1]%2!=0:l.append(a[i-2]+a[i-1]+a[i])
print(len(l), max(l))