a=[int(x) for x in open("data/17-1.txt")]
l=[]
sr=int(sum(a)/len(a))

for i in range(2,len(a)):
    k=0
    if a[i-2]<sr:k+=1
    if a[i-1]<sr:k+=1
    if a[i]<sr:k+=1
    if k>=2:
        if ('1' in str(a[i-2])) and ('1' in str(a[i-1])) and ('1' in str(a[i])):l.append(a[i-2]+a[i-1]+a[i])
print(len(l), max(l))