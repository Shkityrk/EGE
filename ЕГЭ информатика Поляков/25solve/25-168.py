# Автор: А. Кабанов

k, x = 0, 150001
while k!=7:
    sq = int(x**0.5)
    d = set()
    for i in range(2,sq+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    s = sum(d)
    if s%13==10:
        k+=1
        print(x,s)
    x+=1
