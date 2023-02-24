m = ms = k1 = 0
for s in open('K2/24-20.txt'):

    k = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            k += 1
        else:
            k = 1
        ms = max(ms, k)

    if ms > m:
        m = ms
        d = {x: s.count(x) for x in sorted(set(s[:-1]))}

    k1 += s.count('K')

print('K', k1)

