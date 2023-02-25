s=open('24/24var05-08.txt').readline()
while '12' in s: s=s.replace('12', '1 2').replace('21', '2 1')
print(max(len(c) for c in s.split()))