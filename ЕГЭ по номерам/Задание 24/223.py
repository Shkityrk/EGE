s=open('data/24-223.txt').readline()
while 'CACAC' in s: s=s.replace('CACAC','CAC CAC')
s=s.replace('CAC','***').replace('AB', '**')
s=s.replace('A',' ').replace('B',' ').replace('C',' ')
print(max(len(c) for c in s.split()))