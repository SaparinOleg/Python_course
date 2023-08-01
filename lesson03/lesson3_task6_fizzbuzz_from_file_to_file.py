with open('task6_fizzbuzz_task.txt', 'r') as file_in, open('task6_fizzbuzz_solution.txt', 'w') as file_out:
    for line in file_in:
        fizz, buzz, limit = line.split()
        for i in range(1, int(limit) + 1):
            if not i % int(fizz) and not i % int(buzz):
                print('FB', file=file_out, end=' ')
            elif not i % int(fizz):
                print('F', file=file_out, end=' ')
            elif not i % int(buzz):
                print('B', file=file_out, end=' ')
            else:
                print(i, file=file_out, end=' ')
        print('', file=file_out)
