s=open('K/24-5.txt').readline()
s=s.replace('C',' ').replace('F',' ')

print(max(len(c) for c in s.split()))