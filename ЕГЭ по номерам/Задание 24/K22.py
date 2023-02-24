s=open('K/24-22.txt').readline()
s=s.replace('B','A').replace('2','1')

s=s.replace('11A','*').replace('A',' ').replace('1',' ')
print(max(len(c)for c in s.split()))