# Автор: А. Кабанов

k, x = 0, 550001
while k!=5:
    sq = int(x**0.5)
    d = set()
    for i in range(2,sq+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    if len(d)>0:
        f = int(sum(d)/len(d))
        if f%31==13:
            k+=1
            print(x,f)
    x+=1
