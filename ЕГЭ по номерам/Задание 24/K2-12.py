a=[s[:-1] for s in open('K2/24-12.txt').readlines()]
k=0
for s in a:
    if s.count('AOA')>s.count('OAO'):k+=1
print(k)