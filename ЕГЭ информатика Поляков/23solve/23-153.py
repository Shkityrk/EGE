
def rec( n, end ):
 if n < end : return 0
 if n == end: return 1
 return rec(n-8, end) + rec(n//2, end)

print( rec(102, 43) * rec(43, 5) )