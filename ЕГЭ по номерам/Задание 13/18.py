s='АБГД БВГ ВЗКЕ ГВЕЖ ДГ ЕКМИЖ ЖИ ЗЛК ИМ КЛНМ ЛН МН'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:return ('Г' in s)+('Е'  in s)==1
    return sum(f(s+c,e)for c in d[s[-1]])

print(f('А','Н'))