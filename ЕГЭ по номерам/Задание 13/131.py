s='АБ БВ ВЖЕГ ГЕД ДЕЖК ЕЖ ЖНЗ ЗЛКД КЛ ЛМ МАН НАБВ'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:return 1
    return sum(f(s+c,e)for c in d[s[-1]] if c not in s)

print(f('Н','Ж')+f('З','Ж'))