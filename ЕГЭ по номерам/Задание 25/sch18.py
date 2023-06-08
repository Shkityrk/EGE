def f(n):
    s = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s.append(i)
            s.append(n // i)
    return set(s)

for n in range(21514, 30101+1):
    r=f(n)
    if len(r)==3:
        print(min(r),max(r))