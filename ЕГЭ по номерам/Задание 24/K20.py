s=open('K/24-20.txt').readline()
s=s.replace('B','A').replace('2','1')

s=s.replace('A1','*').replace('A',' ').replace('1',' ')
print(max(len(c) for c in s.split()))