const N=10;
var a: array [1..N]of integer;
    a1: array [1..N]of integer;
    i,j, l, min, max, k, m: integer;
    
begin
  for i:=1 to N do begin
    a[i]:= random(100)-50;
  end;
  writeln(a);
  for i:=1 to N do begin
    if a[i]>0 then a1[i]:=0
    else if a[i]<0 then a1[i]:=1
  end;
  writeln(a1);
  
  for i:=1 to N-1 do
    for j:=i+1 to N do 
      if a[i]>a[j] then begin
      l:=a[i];
      a[i]:=a[j];
      a[j]:=l;      
    end;
  writeln(a);
  max:=a[1];
  min:=a[1];
  k:=1; m:=1; 
  for i:=2 to n do begin
    if a[i]>max then begin
      max:=a[i];
      k:=i
    end;
    if a[i]<min then begin
      min:=a[i];
      m:=i; 
    end;  
    end;
    
  a[k]:=min;
  writeln(a);
end.