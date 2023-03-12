s='АБГД БВГ ВИЕГ ГЕЖД ДЖ ЕИМК ЖЕК ИМ КМ'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:return len(s)==7
    return sum(f(s+c,e)for c in d[s[-1]])

print(f('А','М'))