s=open('schelchok/3__1vv4k.txt').readline()

for x in 'BC':
    s=s.replace(x,' ')
s=s.split()
print(len(max(s,key=len)))