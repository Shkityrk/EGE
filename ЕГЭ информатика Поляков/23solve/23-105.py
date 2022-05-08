TARGET = 25

def rec( n, remains ):
 if remains == 0:
   if n == TARGET: return 1
   return 0
 return rec( n+1, remains-1 ) + \
        rec( n+3, remains-1 ) + \
        rec( n*2, remains-1 )

print( rec(2, 7) )