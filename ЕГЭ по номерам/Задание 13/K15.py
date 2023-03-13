s='ABCD BEF CBFGHID DI ELG FEG GLKJM HG IGJ JK KM LM'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:return 'E' in s
    return sum(f(s+c,e)for c in d[s[-1]])

print(f('A','M'))