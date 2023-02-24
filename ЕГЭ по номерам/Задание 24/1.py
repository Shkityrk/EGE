s=open('data/k7/k7-3.txt').readline()
s=s.replace('A',' ').replace('B',' ')
print(max(len(c) for c in s.split()) )