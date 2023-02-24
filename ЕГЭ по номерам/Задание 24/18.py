s=open('data/k7/k7-96.txt').readline()
s=s.replace('A',' ').replace('B', ' ')
print(max(len(c) for c in s.split()))