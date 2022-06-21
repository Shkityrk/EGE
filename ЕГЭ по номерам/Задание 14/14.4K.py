s=51*7**12-7**3-22
k=0
while s!=0:
    k+=s%7
    s//=7
print(k)