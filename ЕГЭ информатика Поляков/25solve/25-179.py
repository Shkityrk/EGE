start = 800000

count = 0
x = start
while count < 5:
  d = 2
  q = round(x**0.5)
  while d <= q:
    if x % d == 0:
      break
    d += 1
  if d <= q and (d + x//d) % 138 == 0:
    print( x, d + x//d )
    count += 1
  x += 1