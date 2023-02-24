s=open('data/24-224.txt').readline()
s=s.replace('BACAB','BAC CAB').replace('CABAC','CAB BAC')
s=s.replace('BAC','***').replace('CAB','***').replace('A',' ').replace('B',' ').replace('C',' ')
print(max(len(c) for c in s.split()))