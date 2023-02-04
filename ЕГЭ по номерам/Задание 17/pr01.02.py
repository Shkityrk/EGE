a=[int(x) for x in open("data/17-1.txt")]
s=[]
sr=int(sum(a)/len(a))

for i in range(2,len(a)):
    if a[i-2]<sr or a[i-1]<sr or a[i]<sr:
        if ('9' in str(a[i-2]) ) and  ('9' in str(a[i-1]) ) and  ('9' in str(a[i]) ):
            s.append(a[i-2]+a[i-1]+a[i])
print(len(s), max(s))
