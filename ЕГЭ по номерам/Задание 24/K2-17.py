s=open('K2/24-17.txt').readline()

d={x:0 for x in sorted(set(s))}

for i in range(len(s)-2):
    if s[i]==s[i+2]:
        d[s[i+1]]+=1
mx=max(d.values())

l=[i for i in d if d[i]==mx]
print(l,mx)