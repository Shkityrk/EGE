s=open('K/24-7.txt').readline()
s=s.replace('XY', 'X Y').replace('XZ', 'X Z')
print(max(len(c) for c in s.split()))