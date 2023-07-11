f = int(input('Enter fizz\n'))
b = int(input('Enter buzz\n'))
lim = int(input('Enter limit\n'))

print(', '.join(['FB' if not i % f and not i % b else 'F' if not i % f else 'B' if not i % b else str(i) for i in range(1, lim+1)]))
input()
