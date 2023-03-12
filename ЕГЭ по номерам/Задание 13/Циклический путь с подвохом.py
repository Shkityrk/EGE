s='АБЖ БВЗ ВГ ГДЖЗ ДКЕАЖ ЕИА ЖЗ ЗАВ ИА КЕ'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:return 1
    return sum(f(s+c,e)for c in d[s[-1]] if c not in s)

print(f('А','З')+f('В','З'))