
allResults = set()
def rec( n ):
 if n > 100: return
 if n % 2 == 0:
   allResults.add( n )
 rec( n+3 )
 rec( n*3 )

rec( 3 )
print( len(allResults) )