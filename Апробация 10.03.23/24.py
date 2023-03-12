f=open('files/24_6757.txt').readline()
f=f.replace('CFE','*').replace('FCE','*').replace('C',' ').replace('D',' ').replace('E',' ').replace('F',' ')
print(max(len(c) for c in f.split()))