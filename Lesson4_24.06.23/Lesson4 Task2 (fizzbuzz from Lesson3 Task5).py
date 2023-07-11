with open('Task2 fizzbuzz (task).txt', 'r') as file:
    for line in file:
        f, b, lim = map(int, line.split())
        print(', '.join(['FB' if not i % f and not i % b else 'F' if not i % f else 'B' if not i % b else str(i) for i in range(1, lim+1)]))
input()
