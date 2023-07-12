number = entered_number = input('Введите целое число\n')
number = number.lstrip("-")
entered_number = entered_number.lstrip('0')
if number.isdecimal():
    number = int(number)
    if not number:
        divider = 0
        print('Да это же ', end='')
    else:
        divider = 1
        print('Число ' + entered_number + ' делится на: ', end='')
    while divider <= number-1:
        if number % divider == 0:
            print(divider, end=', ')
        divider += 1
    print(divider)
else:
    print('Некорректный ввод')
input()
