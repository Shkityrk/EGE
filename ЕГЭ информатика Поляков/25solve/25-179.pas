## uses school;
(800001..maxInt).Select( x->x.Divisors )
  .Where( divs->divs.Count > 2)  
  .Select( divs->(divs[1], divs[^2], divs[^1]))
  .Where( \(d,q,x)->(d+q) mod 138 = 0  )
  .Select( \(d,q,x)-> x + ' ' + (d+q) )
  .Take(5)
  .PrintLines;