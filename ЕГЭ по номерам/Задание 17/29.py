mx=1

s=0
for x in range(2807, 8559):
    if x%2==1 and x//2%2==1 and x%9==5:
        mx=max(mx,x)
        s+=x
print(mx,s)
