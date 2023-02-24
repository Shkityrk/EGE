s=open('data/24-5.txt').readline()
k=0

while '()' in s:
    s=s.replace('()','*')
print(s.count('*'))