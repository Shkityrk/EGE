s='АБГ БДВ ВДЕ ГВЖЗ ДИ ЕИК ЖКЛ ЗЛ ИКМ КМ ЛМ'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:return 1
    return sum(f(s+c,e) for c in d[s[-1]])
print(f('А','М'))