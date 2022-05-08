def f( a, b, prev = 0 ):
  return 0 if a > b else \
         1 if a == b else \
         (0 if prev == 1 else f(a+1, b, 1)) + \
         f(a+2, b, 2) + \
         f(a*2, b, 3)


print( f(1, 18) )