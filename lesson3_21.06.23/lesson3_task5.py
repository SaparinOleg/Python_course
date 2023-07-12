with open('Task6_fizzbuzz(task).txt', 'r') as file:
    for line in file:
        fizz, buzz, limit = line.split()
        for i in range(1, int(limit) + 1):
            if i % int(fizz) == 0 and i % int(buzz) == 0:
                print('FB', end=' ')
            elif i % int(fizz) == 0:
                print('F', end=' ')
            elif i % int(buzz) == 0:
                print('B', end=' ')
            else:
                print(i, end=' ')
        print('')
input()
