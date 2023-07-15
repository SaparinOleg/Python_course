with open('task6_fizzbuzz_task.txt', 'r') as file:
    for line in file:
        fizz, buzz, limit = line.split()
        for i in range(1, int(limit) + 1):
            if not i % int(fizz) and not i % int(buzz):
                print('FB', end=' ')
            elif not i % int(fizz):
                print('F', end=' ')
            elif not i % int(buzz):
                print('B', end=' ')
            else:
                print(i, end=' ')
        print('')
input()
