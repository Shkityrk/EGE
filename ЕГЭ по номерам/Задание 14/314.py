k=0
n=(7**160 * 7**90) - (14**150 + 2**13)
while n!=0:
    if n%7!=6:k+=n%7
    n//=7
print(k)