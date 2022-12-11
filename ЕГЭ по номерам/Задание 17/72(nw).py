def f(n):
    return sum(int(x)\
               for x in str(n)\
               if int(x)>5)
k=0
mx=0
for n in range(2848, 109499+1):
    s=str(n)
    if '9' in s and f(n)%3==0:
        k+=1
        if s[0]=='8':
            mx=max(mx,n)
print(k,mx)
