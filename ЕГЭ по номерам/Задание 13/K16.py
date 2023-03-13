s='АБВГД БЕ ВК ГВЗД ДЗИ ЕКЖ ЖК ЗКИ ИЖ'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:return 'Е' not in s
    return sum(f(s+c,e)for c in d[s[-1]])

print(f('А','К'))