##
uses school;
(800000..801000)
  .Select(x->x.Divisors)
  .Where(dvs->dvs.Count >= 4)
  .Select(dvs->|dvs[1], dvs[^2], dvs[^1]|)
  .Where(dvs-> (dvs[1]+dvs[0]).Divs(138) )
  .Take(5)
  .Select(dvs->|dvs[^1], dvs[1]+dvs[0]|)
  .PrintLines