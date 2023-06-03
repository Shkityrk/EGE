from fnmatch import *
s=open('data/24-230.txt').readline()
for c in 'QWERTYUIOASDFGHJZLXCVBNM':
    s=s.replace(c,' ')
a=[]
s=s.split('KK')
for c in s:
    if ' ' not in c and 'Z' not in c and  fnmatch(c,'43??78???34'):
        a+=[int(c)]
m=max(a)