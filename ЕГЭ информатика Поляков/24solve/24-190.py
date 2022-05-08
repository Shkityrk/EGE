with open('24-181.txt') as f:
   s = f.readline()

for c in 'AEIOUY':
  s = s.replace(c, '_')

parts = s.split('_')
parts.sort( key = len )

parts = [p for p in parts
           if p.count('.') >= 6 ]

print( len(parts[-1]) )
