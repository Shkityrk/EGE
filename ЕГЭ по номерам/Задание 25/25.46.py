start ,end = 326496, 649632
def divs(n):
    s = []
    d = 1
    while d ** 2 <= n:
        if n % d == 0:
            s.append(d)
            if n // d > d:
                s.append(n // d)
        d += 1
    return sorted(s)

for i in range(start,end+1):
    lst= divs(i)
    num_ch=[l for l in lst if l%2==0]
    num_ch_not=[l for l in lst if l%2!=0]
    if len(num_ch)==len(num_ch_not) and len(num_ch)>=70 and len(num_ch_not)>=70:
        print(i, min(d for d in lst if d>=1000))
