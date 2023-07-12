with open('Task2 fizzbuzz (task).txt', 'r') as file_in, open('Task2 fizzbuzz (solution).txt', 'w') as file_out:
    for line in file_in:
        f, b, lim = map(int, line.split())
        print(', '.join(['FB' if not i % f and not i % b else 'F' if not i % f else 'B' if not i % b else str(i) for i in range(1, lim+1)]), file=file_out)
input()
