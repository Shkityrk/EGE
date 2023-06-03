s=open('data/24_7824.txt').readline()
s=s.replace('A','*').replace('B','*').replace('C','*')
while '***' in s:
    s=s.replace('***','** **')
s=s.split()

print(len(max(s,key=len)))