f=[s[:-1] for s in open('data/24-s1.txt').readlines()]
c=0
for s in f:
    for i in range(len(s)-2):
        if s[i]=='F' and s[i+2]=='O':
            c+=1
            break
print(c)