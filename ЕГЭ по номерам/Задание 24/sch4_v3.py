s=open('schelchok/4__1vv4m.txt').readline()
s=s.replace('D',' ')
s=s.split()

print(len(max(s,key=len)))