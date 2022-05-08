# Автор: А. Кабанов

def prime(x):
    sq = int(x**0.5)
    return all(x%i!=0 for i in range(2,sq+1))

k, x = 0, 250001
while k!=5:
    sq = int(x**0.5)
    d = set()
    for i in range(2,sq+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    d = [i for i in d if prime(i)]
    s = sum(d)
    if s%17==0 and s!=0:
        k+=1
        print(x,s)
    x+=1
