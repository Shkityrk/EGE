var i, d, col, sum: int64; 
    sred: double;
     
function prost(x: integer): boolean; 
var j: integer; flag: boolean; 
begin 
     flag := true;
     for j:=2 to round(sqrt(x)) do 
       if x mod j = 0 then begin
         flag := false;
         break;
       end;
     prost:=flag; 
end; 
  
begin     
  sred := 0;   
  sum := 0;
  for d:= 351627 to 428763 do
    for i:=2 to round(sqrt(d)) do 
      if (d mod i = 0) and prost (i) then  begin 
        if (i <> d div i) and prost(d div i) then begin 
          col := col + 1; 
          sred := (sred*(col-1) + d) / col;
          sum := sum + d;
          break;
        end; 
  end; 
 
  writeln( col, ' ', sum div col); 
  writeln( col, ' ', floor(sred) ); 
end.
