s='ABCDE BFG CBGH DCH EDHI FJ GFJK HGK IHKL JM KJLM LM'
d={c[0]:c[1:] for c in s.split()}

def f(s,e):
    if s[-1]==e:return 1
    return sum(f(s+c,e)for c in d[s[-1]])

print(f('A','M'))