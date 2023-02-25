s=open('24/24var05-08.txt').readline()
print(max(len(c) for c in s.split('00'))+2)