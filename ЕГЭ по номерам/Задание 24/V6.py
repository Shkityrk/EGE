s=open('24/24var05-08.txt').readline()
s=s.replace('000', '00 00')
print(max(len(c) for c in s.split()))