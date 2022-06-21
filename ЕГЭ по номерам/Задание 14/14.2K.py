s=3*16**8-4**5+3
k=0
while s!=0:
    if s%4==3: k+=1
    s//=4
print(k)