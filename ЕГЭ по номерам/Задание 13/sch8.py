s='АБВГ БД ВБЕГ ГЕИ ДКЛЖ ЕДЖИ ЖЛМ ИМН КМ ЛКМ МПРС НМ ПС РС С'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:return 1
    return sum(f(s+c,e) for c in d[s[-1]])
print(f('А','Л')*f('Л','С'))