s=open('schelchok/2__1vv4j.txt').readline()

for x in 'ABDE':
    s=s.replace(x,' ')
s=s.split()

print(len(max(s,key=len)))