// Автор: В.Н. Шубинкин

begin
  assign(input, '24-1.txt');
  var s: string;
  read(s);
  var maxlen := 0;
  var pos := 0;
  for var i := 2 to length(s) - 1 do
    if (s[i - 1] > s[i]) and (s[i] < s[i + 1]) then
      if pos = 0 then pos := i
      else 
      begin
        if i - pos > maxlen then maxlen := i - pos;
        pos := i
      end;
  write(maxlen)
end.