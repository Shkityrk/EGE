// Автор В.Н. Шубинкин
##
var s := ReadLines('24-s1.txt').minBy(line -> line.count(c -> c = 'A'));
var max_letter_count := 0;
var letter := '';
for var let := 'A' to 'Z' do
begin
  var let_count := s.Count(c -> c = let);
  Println(let, let_count);
  if let_count >= max_letter_count then
  begin
    max_letter_count := let_count;
    letter := let
  end;
end;
write(letter, ReadAllText('24-s1.txt').Count(t -> t = letter))

// Вместо Count(c -> c = let) можно было бы воспользоваться CountOf(let),
// но на экзамене может быть установлена недостаточно свежая версия PascalABC.NET