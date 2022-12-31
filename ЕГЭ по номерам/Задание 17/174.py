a=[int(x) for x in open("data/17-4.txt")]
s=[]
for i in range(len(a)):
    if a[i]%100//10<=4 and (a[i]%1000//100 in [3,4,5,6,7]):s.append(a[i])
print(len(s), min(s))