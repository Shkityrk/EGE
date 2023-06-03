s='АБВГ БЖДВ ВДЕ ГВЕ ДМЛ ЕДЛК ЖМД ИНТРП КИП ЛМКИ МНИ НТИ ПР РТС СУ ТСУ У'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:return 1
    return sum(f(s+c,e)for c in d[s[-1]])
print(f('А','Л')*f('Л','У'))