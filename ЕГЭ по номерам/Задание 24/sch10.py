s=open('schelchok/3__1vf5x.txt').readline()

s=s.replace('BBDEC','*****')
for i in range(1,len(s)):
    if s[i]=='*':
        print(i)