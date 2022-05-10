def p(n):
    s=[]
    for x in range(1,n+1):
        if n%x==0:
            s.append(x)
    return s
print(sum(p(2021)))
print(len(p(2021)))
print(sum(p(2021))-len(p(2021)))