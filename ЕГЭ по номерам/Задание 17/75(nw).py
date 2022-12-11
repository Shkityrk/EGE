def f(n):
    s=0
    while n!=0:
        s+=n%10
        n//=10
    return s

l=[3**x for x in range(50) ]
s=[]
for i in l:
    if len(str(i))> len(set(str(i))):
        s.append(i)
k=0
mx_sum=0
mn=10**10
for n in range(138, 603885):
    if any(n==z for z in s):
        k+=1        
        if f(n)>mx_sum:
            mx_sum=f(n)
            mn=n

        
print(k,mn)
