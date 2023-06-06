for n in range(1, 1000):
    b = bin(n)[2:]
    s = str(b)
    if s.count('1') % 2 == 0:s = s + '0'
    else:s = s + '1'
    if s.count('1') % 2 == 0:s = s + '0'
    else:s = s + '1'
    r = int(s, 2)
    if r > 255:
        print(r)
        break