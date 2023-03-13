s='АБВ БВГ ВГ ГДЕЖЗ ДЕИ ЕИКЗ ЖЗЛ ЗКЛ ИКМ КМ ЛКМ'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:return 'Е' in s
    return sum(f(s+c,e) for c in d[s[-1]])

print(f('А','М'))