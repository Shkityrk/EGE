// Автор: А. Богданов
### uses school;
(97*97*97+1..maxint).Sel(x->(x,x.Divisors))
.Sel(\(x,d) -> (x,d.Wh(i->(i mod 10=3)and(i in 100..999)).ToA))
.Wh(\(x,d) -> d.Len=3)
.Take(5).PrintLines;