
allResults = set()
def rec( n, remains ):
 if remains == 0:
   allResults.add( n )
   return
 rec( n+1, remains-1 )
 rec( n*2-3, remains-1 )

rec( 3, 12 )
print( len(allResults) )


