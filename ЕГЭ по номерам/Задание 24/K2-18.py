s=open('K2/24-18.txt').readline()

d={x:0 for x in sorted(set(s))}

for i in range(len(s)-4):
    if s[i]+s[i+1]=='CB' and s[i+3]+s[i+4]=='BC':
        d[s[i+2]]+=1
m=max(d.values())
l=[i for i in d if d[i]==m]
print(l,m)