def f(n):
    s=0
    for x in range(2,int(n**0.5)+1):
        if n%x==0:
            s=1
    if s==0: return 1
k=0
mx=0
for i in range(2095, 19402):
    s=str(i)
    if f(i) and int(s[0])>int(s[-1]):
        k+=1
        if s[-2:]=='21':
            mx=max(mx,i)

print(k,mx)
