from fnmatch import *
s=open('data/24-230.txt').readline()
for c in 'QWERTYUIOASDFGHJKLXCVBNM':
    s=s.replace(c,' ')
a=[]
s=s.split('ZZ')
for c in s:
    if ' ' not in c and 'Z' not in c and  fnmatch(c,'8???54???22'):
        a+=[int(c)]
m=max(a)

p=1
while m>0:
    if (m%10)%2!=0:
        p*=m%10
    m//=10
print(p)