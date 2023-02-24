f=[s[:-1] for s in open('data/24-s1.txt').readlines()]
c=0
for s in f:
    if s.count('J')>s.count('E'):c+=1
print(c)