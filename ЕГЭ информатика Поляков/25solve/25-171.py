# Автор: А. Кабанов

def prime(x):
    sq = int(x**0.5)
    return all(x%i!=0 for i in range(2, sq+1))

k, x = 0, 450001
while k!=4:
    sq = int(x**0.5)
    d = set()
    for i in range(2,sq+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    d = [i for i in d if prime(i)]
    if len(d)>0:
        m = max(d) - min(d)
        if m%29==11:
            k+=1
            print(x,m)
    x+=1
