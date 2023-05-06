f=open('24.txt').readline()
f=f.replace('A','*').replace('B','*').replace('C','*')
for c in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    f=f.replace(c,'_')
f=f.split('_')
print(max(f))