# Автор: А. Кабанов

k, x = 0, 350001
while k!=6:
    sq = int(x**0.5)
    d = set()
    for i in range(2,sq+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    if len(d)>0:
        m = max(d) - min(d)
        if m%23==9:
            k+=1
            print(x,m)
    x+=1
