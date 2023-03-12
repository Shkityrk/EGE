s='АБВГ БД ВБДЕЗЖГ ГЖ ДЕ ЕЗ ЖЗ'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:
        print(s)
        return 1
    return sum(f(s+c,e) for c in d[s[-1]])
print(f('А','З'))