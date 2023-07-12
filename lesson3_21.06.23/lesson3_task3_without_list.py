amount = int(input('Будь ласка, введіть бажану суму кратну 10:\n'))
print('\nОтримайте гроші:')

exception = amount % 10
banknote = 1000
quantity = amount // banknote
exponent = 100

while banknote >= 10:
    if not (banknote // 2) // exponent:
        exponent //= 10
    if quantity > 0:
        print(str(banknote) + 'грн x' + str(quantity))
        amount -= quantity * banknote
    banknote = (banknote // 2) // exponent * exponent
    quantity = amount // banknote

if exception:
    print(f"\nЗалишок {exception} грн на ЗСУ")

input('\nНатисніть Enter\n')
