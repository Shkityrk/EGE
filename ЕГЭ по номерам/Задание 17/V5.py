a=[int(x) for x in open("17/17var05.txt")]
l=[]

n=[x**2 for x in range(1,10000)]

for i in range(1,len(a)):
    if a[i-1] in n or a[i] in n:
        l.append(a[i-1]+a[i])
print(len(l), max(l))