s='АБВГД БЕВ ВЖ ГВЖ ДГЖЗ ЕЖИ ЖИ ЗЖИ ИКЛ КМ ЛКМ'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:  return len(s)-1
    return max(f(s+c,e)for c in d[s[-1]])

print(f('А','М'))