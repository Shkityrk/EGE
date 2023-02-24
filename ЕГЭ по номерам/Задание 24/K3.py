s=open('K/24-2.txt').readline()
s=s.replace('D', ' ')
print(max(len(c) for c in s.split()))