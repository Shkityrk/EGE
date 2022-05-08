def pr(n):
    p=1
    for l in n:
        p=p*l
    return p

def num(n):
    s=[]
    while n!=0:
        s.append(n%10)
        n=n//10

    return s[::-1]
for i in range(87921, 88187):
    print( pr( num(i)))