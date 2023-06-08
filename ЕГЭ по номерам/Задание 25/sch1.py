def d(n):
    s=[]
    s.append(1)
    s.append(n)
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.append(i)
            s.append(n//i)
    return len(s)
mx=0

for n in range(64032,64131):
    mx=max(d(n),mx)
for n in range(64032,64131):
    if d(n)==mx:
        print(mx,n)
        break