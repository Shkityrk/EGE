// Автор: С.П. Пуляшкина
##
uses school;

var z:=(834567..1143210); 
foreach var i in z do begin
  var v := i.Divisors.Except(|1,i|);
  var d := 0;
  var p := -100;// d - количество подходящих, p - первый делитель
  foreach var j in v do begin
    if ((j-p)=2) then  d += 1;
    p := j;
  end;
  if (v.Count>1) and (d=v.Count-1) then 
    Println( i, v.Max );
end