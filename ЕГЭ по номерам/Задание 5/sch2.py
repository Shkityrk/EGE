for n in range(1, 1000):
    r = bin(4 * n)[2:]
    r = r + str(r.count('1') % 2)
    r = r + str(r.count('1') % 2)
    r = int(r, 2)
    if r > 211:
        print(n)
        break