s='АБГД БВГ ВЗКЕ ГВЕЖ ДГ ЕКМИЖ ЖИ ЗЛК ИМ КЛНМ ЛН МН'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:
        if len(s)==8:print(s)
        return 1
    return sum(f(s+c,e) for c in d[s[-1]] )

f('А','Н')

#:)))