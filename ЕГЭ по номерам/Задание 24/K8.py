s=open('K/24-8.txt').readline()
while 'PP' in s:s=s.replace('PP', 'P P')
print(max(len(c) for c in s.split()))