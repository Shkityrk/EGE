s=open('data/24_8431.txt').readline()
s=s.replace('X','*').replace('Y','*').replace('Z','*')
s=s.split('*')
print(len(max(s,key=len)))