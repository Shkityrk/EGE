with open('24-191.txt') as F:
  s = F.readline()

chunks = [ ch for ch in s.split('A')[1:-1]
             if len(ch) >= 15 and 'B' not in ch ]
print( len(chunks) )

