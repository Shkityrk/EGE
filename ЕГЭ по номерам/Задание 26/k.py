f=[c[:-1] for c in open('data/26-j1.txt').readlines()]
f=f[1:]
k=0
for s in range (len(f)-1):
    for j in range(s+1,len(f)):
        if int(f[s])+int(f[j])==100:
            k+=1
            f[s]='0'
            f[j]='0'
print(k)
