
kol=0
for n in range(1,457001):
    if (n%37==0) and (n%5!=0) and (n%19!=0):
        kol+=1
        print(n)
print(kol)