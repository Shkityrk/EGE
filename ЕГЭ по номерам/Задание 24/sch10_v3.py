s=open('schelchok/10__1vv4t.txt').readline()
s=s.replace('EF','**')

for x in 'ABCDEF':
    s=s.replace(x,' ')
s=s.split()

print(len(max(s,key=len)))
print(max(s,key=len))