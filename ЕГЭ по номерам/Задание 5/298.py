def f(b):
    while '0' in b:
        b=b.replace('0',"",1)
    return b+'1'
k=0
for n in range(1,1000):
    b=bin(n)[2:]
    if b.count('1')%2==0: b=b[1:]
    else: b=f(b)
    if b.count('1') % 2 == 0:b = b[1:]
    else: b = f(b)

    r=int(b,2)
    if r==7:k+=1
print(k)
