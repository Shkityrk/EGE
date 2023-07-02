f=open()
n=int(f.readline())
k=int(f.readline())
a=[int(x) for x in f.readlines()]
min_pred=[10**20]*n
min_pred2=[10**20]*(n-k)
otv=10**20

for i in range(n):
    min_pred[i]=min(min_pred[i-1], a[i])
for i in range(k,n):
    min_pred2[i]=min(min_pred2[i-1], a[i]*min_pred[i-k])
for i in range(k,n):
    otv=min(otv, min_pred2[i-k]*a[i] )