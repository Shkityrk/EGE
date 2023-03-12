s='АВЗ БАГ ВЗКЕБ ГА ДАГ ЕБ ЖИ ЗИЖК ИД КЕЖ'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if len(s)>1 and s[-1]==e:return 1
    return sum(f(s+c,e)for c in d[s[-1]])
print(f('А','А'))