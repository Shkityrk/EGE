// Автор В.Н. Шубинкин
##
// Не эффективный, но возможный подход к решению задачи
var line := ReadAllText('24-J1.txt');
var t := 'КОТ';
var target := t;
while target in line do
  target += t;
target := target[:^3];
print(target.length div 3)