with open('24-181.txt') as f:
   s = f.readline()

parts = s.split('.')
parts.sort( key = len )
parts = [p for p in parts if p.count('A') >= 3]
print( len(parts[-1]) )
