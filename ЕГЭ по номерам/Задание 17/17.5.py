f=open ("3 (1).txt")
a=[]
for s in f:
    a.append(int(s))
index_local_mx=0
index_last_local_mx=0
mx=-1
kol=0
for i in range(2, len(a)-2):

    if a[i-1] < a[i] > a[i+1]:
        index_last_local_mx=index_local_mx
        kol+=1
        index_local_mx=i
        if index_local_mx-index_last_local_mx>mx:
            mx=index_local_mx-index_last_local_mx
print(kol,mx)