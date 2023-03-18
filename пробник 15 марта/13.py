s='АБ БВ ВЖЕГ ГЕД ДКЖЕ ЕЖ ЖНЗ ЗДКЛ КЛ ЛМ МНА НАБВ'

d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:
        F=1
        for l in 'АБВГДЕЗКЛМН':
            if s.count(l)>1:
                F=0
                break
        if F==1:return 1
    return sum(f(s+c,e) for c in d[s[-1]])
print(f('Ж','Ж'))