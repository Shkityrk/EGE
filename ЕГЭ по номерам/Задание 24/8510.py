s=open('data/24_8510.txt').readline()
s=s.replace('N','*').replace('O','*').replace('P','*')
while '**' in s:
    s=s.replace('**','* *')

s=s.split()
print(len((max(s,key=len))))