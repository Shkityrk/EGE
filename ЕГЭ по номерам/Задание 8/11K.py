from itertools import product
k=0
for x in product('1234',repeat=4):
    s=''.join(x)
    if int(s[0])<=int(s[1])<=int(s[2])<=int(s[3]):
        k+=1
        print(s)
print(k)