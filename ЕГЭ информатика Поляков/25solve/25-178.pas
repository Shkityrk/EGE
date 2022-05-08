## uses school;
(500001..maxInt).Select( x->x.Divisors )
  .Select( divs->(divs[^1], 
         divs.Where( d->(d mod 10 = 8) and
                        (d in 18..(divs[^1]-1))).ToArray ) )
  .Where( \(x,d)->d.Count > 0  )
  .Select( \(x,d)-> x + ' ' + d[0] )
  .Take(5)
  .PrintLines;