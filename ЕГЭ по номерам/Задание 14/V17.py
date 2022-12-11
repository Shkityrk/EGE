x=7**80+49**15-49
k=0
while x!=0:
    if x%7==6:k+=1
    x//=7
print(k)