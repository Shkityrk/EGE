from itertools import permutations
k=0
for x in permutations('ДЕЙКСТРА', r=6):
    s=''.join(x)
    if any(n in s for n in ['ЙД','ЙК','ЙС','ЙТ','ЙР']):
        k+=1
        print(s)
print(k)