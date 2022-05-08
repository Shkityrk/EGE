def f( a, b, prev = 0 ):
  return 0 if a > b else \
         1 if a == b else \
         f(a+1, b, 1) + f(a+3, b, 2) + \
           (0 if prev == 3 else f(a*2, b, 3))


print( f(1, 14) )