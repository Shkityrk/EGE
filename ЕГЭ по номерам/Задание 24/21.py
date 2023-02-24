s=open('data/k7/k7a-1.txt').readline()
s=s.replace('D', ' ').replace('E', ' ')
print(max(len(c) for c in s.split()))