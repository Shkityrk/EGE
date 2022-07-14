mx=-100
for a in range(1,10000):
    f=1
    for x in range(1,1000):
        f*=(x%a!=0)<=((x%24!=0)and (x%36!=0))
    if f==1:
        mx=max(mx,a)
print(mx)