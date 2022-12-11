with open('data/17-1.txt') as f:
    a = [int(x) for x in f.readlines()]
k=0
for i in range(len(a)-1):
    if (a[i]%9==0 and abs(a[i+1])%8==3 and a[i+1]%9!=0)or\
       (a[i]%9!=0 and abs(a[i])%8==3 and a[i+1]%9==0):k+=1
print(k)
        
