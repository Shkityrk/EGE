// Автор: С.П. Пуляшкина
##
uses school;
var z:=(326496..649632).Where(
       x -> (x.Divisors.Count > 139) 
          and (x.Divisors.Where(y ->y.isEven).count = x.Divisors.Where(a ->a.isOdd).Count));
foreach var x in z do 
  Println( x, x.Divisors.Where(y->y>1000).First );

