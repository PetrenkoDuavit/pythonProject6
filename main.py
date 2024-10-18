# homeworck 6.1

import string

ALL_LETTERS = string.ascii_letters
SEPARATOR = "-"

user_input = input("Enter letters in format: 'a-c' ").strip()  # удаляю лишние пробелы из инпута

if len(user_input) == 3: # проверка размена строки
    first_letter = user_input[0]
    second_letter = user_input[2]
    separator = user_input[1]

    if first_letter.isalpha() and second_letter.isalpha() and separator == SEPARATOR: # проверка присутствия букв и раздилителя
        start_index = ALL_LETTERS.index(first_letter)
        end_index = ALL_LETTERS.index(second_letter)

        if start_index > end_index: # если буквы написаны не по порядку меняю местами
            start_index, end_index = end_index, start_index

        result = ALL_LETTERS[start_index:end_index + 1] # запись в результата в переменную
        print(result)

# homeworck 6.2

days = 0
horas = 0
minutes = 0
test_input = True
while test_input:
    seconds = int(input("Enter seconds:"))
    if seconds < 0 or seconds > 8640000:   # проверка условий задния
        print("Enter enother nomber")
    else:
        test_input = False
if seconds > 86400:      # проверка хватает количество секунд для подсчета дней
    days = seconds // 86400 # узнаю количество дней
    seconds = seconds  % 86400 # остаток записую обратно в переменную
if seconds > 3600:
    horas = seconds // 3600
    seconds = seconds % 3600
if seconds > 60:
    minutes = seconds // 60
    seconds = seconds % 60
print(f"{days} days, {horas}:{minutes}:{seconds}")

# homeworck 6.3

number = int(input("Enter your number:"))

while number > 9:   # прог будет работать пока не останется одна цифра
    temp_number = str(number)
    number = 1 # очистка переменной для нового перемножения
    print(number)
    for char in temp_number: # цикл который пройдется по строке
        if char.isdigit(): # что строка состоит из цифр
            number *= int(char) # перемножение
    print(number)



