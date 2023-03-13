s='АБВГД БЕВ ВЖ ГВЖ ДГЖЗ ЕЖИ ЖИ ЗЖИ ИКМЛ КМ ЛМ'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:return ('Ж' in s and 'К' not in s)
    return sum(f(s+c,e)for c in d[s[-1]])

print(f('А','М'))