s=64**30+2**300-4
n=0
while s!=0:
    if s%8==7: n+=1
    s=s//8
print(n)