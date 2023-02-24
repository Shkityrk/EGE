m=''
s1=''
for s in open('K2/24-19.txt'):
    if s.count('Q')>=m.count('Q'):m=s.strip()
    s1+=s.strip()

d={x:m.count(x) for x in sorted(set(m)) if m.count(x)!=0}

m=min(d.values())
l=[i for i in d if d[i]==m]
print(l,m)
print('c', s1.count('C'))