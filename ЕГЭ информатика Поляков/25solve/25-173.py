# Автор: А. Кабанов

def prime(x):
    sq = int(x**0.5)
    return all(x%i!=0 for i in range(2,sq+1))

k, x = 0, 650001
while k!=4:
    sq = int(x**0.5)
    d = set()
    for i in range(2,sq+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    d = [i for i in d if prime(i)]
    if len(d)>0:
        f = int(sum(d)/len(d))
        if f%37==23:
            k+=1
            print(x,f)
    x+=1
