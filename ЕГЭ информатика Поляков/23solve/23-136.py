def f( a, b ):
  if a == b: return 1
  if a > b: return 0
  return f( a+1, b ) + \
         f( int('1'+f"{a:b}", 2), b)

def g( a, b ):
  if a == b: return 1
  if int(a,2) > int(b,2): return 0
  return g( bin(int(a,2)+1)[2:], b ) + \
         g( '1'+a, b )

print( f(1, 31) )
print( g('1', '11111') )