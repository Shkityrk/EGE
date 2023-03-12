s='АБГДЕ БВ ВИЖ ГБВЖД ДЖЗ ЕДЗК ЖЛ ЗЖЛ ИЖЛ КЗЛМ МЛ'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:return 'Ж' in s and 'З' not in s
    return sum(f(s+c,e) for c in d[s[-1]])
print(f('А','Л'))