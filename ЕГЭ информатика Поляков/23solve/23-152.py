
def rec( n, end, noPoint ):
 if n > end or n in noPoint: return 0
 if n == end: return 1
 return rec(n+1, end, noPoint) + rec(n+2, end, noPoint)

print( rec(11, 29, []) - rec(11, 29, [17, 23]) )