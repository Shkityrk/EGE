f=open('27-12b.txt')
n=int(f.readline())


k6=k2=k3=k=0
for i in range(n):
    x=int(f.readline())
    if x%6==0:k6+=1
    elif x%3==0:k3+=1
    elif x%2==0:k2+=1
    else:k+=1
print(k6*(k6-1)//2 + k6*(n-k6) + k2*k3)