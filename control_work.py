n = 1
string = [0] * n
string = (input('Введите массив: '))
for i in range(n):
   print(string)
word_list = string.split(",")
count = len(word_list)
print("количество введенных строк:", count)
print("Новый массив:")
if count <= 3:
   print(word_list[1:count])
elif count > 3:
   print(word_list[count - count: 3])