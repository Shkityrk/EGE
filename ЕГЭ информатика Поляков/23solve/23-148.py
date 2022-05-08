
allResults = set()
def rec( n, remains ):
 if remains == 0:
   allResults.add( n )
   return
 rec( n+3, remains-1 )
 rec( n*2+1, remains-1 )

rec( 2, 13 )
print( len(allResults) )