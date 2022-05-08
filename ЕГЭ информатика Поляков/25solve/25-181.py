def allDivs( x ):
  divs = [1, x]
  d = 2
  while d*d <= x:
    if x % d == 0:
      divs.append( d )
      if x // d > d:
        divs.append( x//d )
    d += 1
  return sorted(divs)

x = 97**3 # 97 - максимальное двухначное простое число
for count in range(5):
  while True:
    x += 1
    d3 = [d for d in allDivs(x)
            if 100 <= d < 1000 and d % 10 == 3]
    if len(d3) == 3:
      print( x, min(d3) )
      break
