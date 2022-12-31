a=[int(x) for x in open("data/17-4.txt")]
s=[]
for i in range(len(a)):
    if (a[i]%100//10+a[i]%10)>=15 and all(a[i]%x!=0 for x in [3,4,7]):s.append(a[i])
print(min(s),sum(s))