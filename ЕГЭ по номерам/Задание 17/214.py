a=[int(x) for x in open("data/17-4.txt")]
sr=int(sum(a)/len(a))
l=[]

for i in range(1,len(a)):
    if a[i-1]<sr and a[i]<sr and (abs(a[i-1])+abs(a[i]))%100==19:l.append(a[i]+a[i-1])

print(len(l), min(l))