fizz = int(input('Enter fizz\n'))
buzz = int(input('Enter buzz\n'))
limit = int(input('Enter limit\n'))

"""
# Решение через цикл while
counter = 1
while counter <= limit:
    if not counter % fizz and not counter % buzz:
        print('FB', end=' ')
    elif not counter % fizz:
        print('F', end=' ')
    elif not counter % buzz:
        print('B', end=' ')
    else:
        print(counter, end=' ')
    counter += 1
input()
"""


# Решение через цикл for
for i in range(1, limit+1):
    if not i % fizz and not i % buzz:
        print('FB', end=' ')
    elif not i % fizz:
        print('F', end=' ')
    elif not i % buzz:
        print('B', end=' ')
    else:
        print(i, end=' ')
input()
