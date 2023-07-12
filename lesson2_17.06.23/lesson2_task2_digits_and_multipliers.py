number = input('Enter a number\n')
if number.isdecimal():
    number = int(number)
    exponent_of_number = 1
    while not 0 <= number // exponent_of_number < 10:
        exponent_of_number *= 10
    while exponent_of_number >= 10:
        digit_of_number = number // exponent_of_number
        print(str(digit_of_number) + '*' + str(exponent_of_number), end=' + ')
        number %= exponent_of_number
        exponent_of_number //= 10
    print(str(number) + '*1')
else:
    print('Incorrect input')
input()
