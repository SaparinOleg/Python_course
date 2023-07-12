with open('Task6_fizzbuzz(task).txt', 'r') as file_in, open('Task6_fizzbuzz(solution).txt', 'w') as file_out:
    for line in file_in:
        fizz, buzz, limit = line.split()
        for i in range(1, int(limit) + 1):
            if i % int(fizz) == 0 and i % int(buzz) == 0:
                print('FB', file=file_out, end=' ')
            elif i % int(fizz) == 0:
                print('F', file=file_out, end=' ')
            elif i % int(buzz) == 0:
                print('B', file=file_out, end=' ')
            else:
                print(i, file=file_out, end=' ')
        print('', file=file_out)
