s=open('schelchok/1__1vv4i.txt').readline()
s=s.replace('DEBAC','*****',1)

s=s.replace('DEBAC','/////')

for i in range(len(s)):
    if s[i]=='/':
        print(i+1)
        break
