def reverse(n):
    return n[::-1]

for n in range(100,1000):
    b=bin(n)[2:]
    b=reverse(b)
    while b[0]!='1':
        b=b.replace(b[0],"",1)

    r=int(b,2)
    if r==7:
        print(n)