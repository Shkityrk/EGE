s = ['К', 'И', 'Т', 'К', 'А', 'Т']
kol = 0
for a1 in (s):
    for a2 in (s):
        for a3 in (s):
            for a4 in (s):
                for a5 in (s):
                    for a6 in (s):
                        n = a1 + a2 + a3 + a4 + a5 + a6
                        if not 'КК' in n or not 'ТТ' in n:
                            kol += 1
print(kol)
