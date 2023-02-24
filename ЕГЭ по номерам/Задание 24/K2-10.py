a=[s[:-1] for s in open('K2/24-10.txt').readlines()]
k=0
for s in a:
    if s.count('B')/s.count('A')>=1.05:k+=1
print(k)