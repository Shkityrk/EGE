s=open('K2/24-16.txt').readline().strip()

d={x:s.count(x) for x in sorted(set(s))}

mx=max(d.values())
mn=min(d.values())
print(mx-mn)