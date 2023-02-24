s=open('K/24-14.txt').readline()
s=s.replace('D',' ')
c=0
print(min(len(c) for c in s.split())+2)