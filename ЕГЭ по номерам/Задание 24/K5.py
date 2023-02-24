s=open('K/24-6.txt').readline()
s=s.replace('A',' ').replace('B',' ').replace('C',' ')
print(max(len(c) for c in s.split()))