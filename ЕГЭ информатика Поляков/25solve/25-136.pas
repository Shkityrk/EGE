// Автор: С.П. Пуляшкина
##
uses school;
var x := 0;
var z := (25317..51237).Where(
       x -> (x.Factorize.Distinct.count>5));
foreach var i in z do
  Println( i, i.Factorize.Max )