start = 500000

count = 0
x = start
while count < 5:
  d = 18
  while d < x:
    if x % d == 0:
      break
    d += 10
  if d < x:
    print( x, d )
    count += 1
  x += 1