start = 3000000
end = 10000000

#start, end = 1, 100
count = 0

primes = [1]*(end+1);
for d in range(2, round(end**0.5)):
  if primes[d]:
    for k in range(2*d,end+1,d):
      primes[k] = False;

#print( [x for x in range(start,end+1) if primes[x]] )

count = 0
avg = 0
for x in range(start,end-1):
  if primes[x] and primes[x+2]:
    count += 1
    avg = x + 1
    #print( x, x+2 )

print( count, avg )