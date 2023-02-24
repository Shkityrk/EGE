s=open('data/k7/k7a-5.txt').readline()
s=s.replace('C',' ').replace('F', ' ')
print(max(len(c) for c in s.split()))