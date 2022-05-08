// Автор: С.П. Пуляшкина
##
uses school;
var z:=(523456..578925).Where(x -> (x.Factorize.Count=2) and (x.Divisors.Count=4)); 
var m:=1000000;
var v:=1000;
foreach var x in z do 
  if (x.Factorize.Last-x.Factorize.First) < m 
  then begin 
    m := x.Factorize.Last - x.Factorize.First;
    v := x;
  end;
   
Println( v.Factorize );

