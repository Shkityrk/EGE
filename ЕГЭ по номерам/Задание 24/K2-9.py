a=[s[:-1] for s in open('K2/24-9.txt').readlines()]
k=0
for s in a:
    if s.count('S')==s.count('X'):k+=1
print(k)