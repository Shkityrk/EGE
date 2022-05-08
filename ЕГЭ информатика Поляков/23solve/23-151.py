
def rec( n, end ):
 if n > end: return 0
 if n == end: return 1
 if n % 2 == 0:
   res3 = rec( n + 1, end )
 else:
   res3 = rec( n + 2, end )
 return rec(n+1, end) + rec(n*2, end) + res3

print(rec(3,6))

print(rec(3,9))
print(rec(9,17))
print(rec(17,25))
print( rec(3, 9)*rec(9, 17)*rec(17, 25) )