s='АВ БАГЖ ВДБ ГЖ ДЗ ЖДЗ ЗБВ'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:return 1
    return sum(f(s+c,e) for c in d[s[-1]] if s.count(c)<=1)
print(f('Ж','Г'))