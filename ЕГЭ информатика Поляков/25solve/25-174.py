start = 1
end = 5000
count = 0
maxTri = (0, 0, 0)
maxA = round( (end**2/2)**0.5 )
for a in range(start, maxA+1):
  maxB = round( (end**2-a**2)**0.5 )
  for b in range(a+1, maxB+1):
    c2 = a**2 + b**2
    c = round(c2**0.5)
    if b <= end and c**2 == c2:
      #print(a, b, c)
      count += 1
      if a+b+c > sum(maxTri):
        maxTri = (a, b, c)

print( count, maxTri )