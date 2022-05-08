
bad = [12]

def rec( start, end ):
  if start > end or start in bad: return 0
  if start == end: return 1
  return rec( start+1, end ) + \
         rec( start+3, end ) + \
         rec( start*2, end )

print( rec(3,8)*rec(8,21) )