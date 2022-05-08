##
var ABC := 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
var data := ReadLines('24-164.txt').ToArray;
var maxK := 0;
var letterMax := '';
foreach var s in data do begin
    var (k, currK) := (1, 1);
    for var i:=2 to length(s) do
      if s[i] = s[i-1] then begin
        currK += 1;
        k := max(k, currK);
      end
      else
        currK := 1;
    if k > maxK then begin
      maxK := k;
      var ma := 0;
      foreach var letter in ABC do begin
        var cnt := s.CountOf(letter);
        if cnt > ma then
          (ma, letterMax) := (cnt, letter);
      end;
    end;
end;

Print( letterMax );
data.Select( s->s.Count(x->x=letterMax)).Sum.Println;
