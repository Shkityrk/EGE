k=0
mn=100000
for n in range(1000, 10000):
    a=n
    s=0
    while a!=0:
        s+=1
        a//=5 
    if s>=6 and (n%25==11 or n%25==13):
        k+=1
        mn= min(mn,n)
print(k,mn)
