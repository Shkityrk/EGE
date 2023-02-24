s=open('K/24-1.txt').readline()
s=s.replace('C',' ').replace('D',' ')
print(max(len(c) for c in s.split()))