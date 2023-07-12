fizz = int(input('Enter fizz\n'))
buzz = int(input('Enter buzz\n'))
limit = int(input('Enter limit\n'))

"""
#Решение через цикл while
counter = 1
while counter <= limit:
    if counter % fizz == 0 and counter % buzz == 0:
        print('FB', end=' ')
    elif counter % fizz == 0:
        print('F', end=' ')
    elif counter % buzz == 0:
        print('B', end=' ')
    else:
        print(counter, end=' ')
    counter += 1
input()
"""


#Решение через цикл for
for i in range(1, limit+1):
    if i % fizz == 0 and i % buzz == 0:
        print('FB', end=' ')
    elif i % fizz == 0:
        print('F', end=' ')
    elif i % buzz == 0:
        print('B', end=' ')
    else:
        print(i, end=' ')
input()
