s=open('24/24var05-08.txt').readline()
s=s.replace('12', '1 2').replace('13', '1 3').replace('31', '3 1').replace('21', '2 1')
print(max(len(c) for c in s.split()))