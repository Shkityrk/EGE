def f(n):
    s=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.append(i)
            s.append(n//i)
    s.sort()
    return s
for n in range(500001,500034):
    s=f(n)
    for i in s:
        if i%10==8 and i!=8:
            print(n,i)
            break