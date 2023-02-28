f = open('17data/17-343.txt')
f = [i.strip() for i in f.readlines()]
mn = 100000000
k = 0
for i in range(len(f)-2):
    a, b, c = f[i], f[i+1], f[i+2]
    y = 1
    for n in [a, b, c]:
        sm_ch = sm_nch = 0
        for i in range(0, len(n), 2):
            sm_nch += int(str(n)[i])
        for i in range(1, len(n), 2):
            sm_ch += int(str(n)[i])
        if sm_ch != 0:
            if sm_nch % sm_ch != 0:
                y = 0
        else:
            y = 0
    if y:
        k += 1
        mn = min(int(a)+int(b)+int(c), mn)
print(k, mn)
    
