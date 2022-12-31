a=[int(x) for x in open("data/17-338.txt")]
mn=min(a)
l=[]

for i in range(1,len(a)):
    if a[i-1]%117==mn or a[i]%117==mn:l.append(a[i-1]+a[i])
print(len(l), max(l))