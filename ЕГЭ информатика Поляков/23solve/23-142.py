
bad = [14]

def rec( start, end ):
  if start > end or start in bad: return 0
  if start == end: return 1
  return rec( start+1, end ) + \
         rec( start+2, end ) + \
         rec( start*3, end )

print( rec(1,10)*rec(10,15) )