s= open('24data/k7-0.txt').readline()
s.replace('A', ' ').replace('B', ' ')
n= max(s.split(), key=len)
print(len(n))