s=open('K/24-9.txt').readline()
while 'XZZY' in s: s=s.replace('XZZY', 'XZZ ZZY')
print(max(len(c) for c in s.split()))