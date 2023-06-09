s=open('schelchok/4__1vf5y.txt').readline()

for x in 'BCED':
    s=s.replace(x,' ')
s=s.split()
print(len(max(s, key=len)))