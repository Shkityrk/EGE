uses school;
begin
  var startN := 55000000;
  var endN := 60000000;
  for var x0:=startN to endN do begin
    var x:= x0;
    while x.IsEven do x:= x div 2;
    var qX := round(sqrt(sqrt(x)));
    if qX.IsPrime and (qX*qX*qX*qX = x) then
      Println( x0, x );    
  end;
end.
