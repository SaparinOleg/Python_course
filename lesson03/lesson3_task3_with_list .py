amount = int(input('Будь ласка, введіть бажану суму кратну 10:\n'))
print('\nОтримайте гроші:')
exception = amount % 10

denominations = [1000, 500, 200, 100, 50, 20, 10]
for banknote in denominations:
    quantity = amount // banknote
    if quantity:
        print(f'{banknote}грн x {quantity}')
        amount -= quantity * banknote

if exception:
    print(f"\nЗалишок {exception} грн на ЗСУ")

input('\nНатисніть Enter\n')
