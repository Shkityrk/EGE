// Автор: С.П. Пуляшкина
##
uses school;

var z:=(2000000..3000000);
foreach var i in z do begin
  var v := i.Divisors.Distinct;
  var d:=0;
  var m:=0; // d - количество подходящих, m - максимальный сомножитель
  foreach var j in v do 
     if abs(j-(i div j))<=120 then begin 
       d += 1;
       m := max( m, j, i div j );
     end;
  if d>=6 then 
    Println( i, m );
end