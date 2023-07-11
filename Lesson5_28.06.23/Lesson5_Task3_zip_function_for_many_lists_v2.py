def mega_zip(*args):
    return [] if not args else [tuple(lis[i] for lis in args) for i in range(min([len(lis) for lis in args]))]


test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
test3 = [1, 2, 3, 4, 5]
test4 = ['a', 'b', 'c', 'd', 'e', 'f']
test5 = [True, False, True, False, True, False, False]
test6 = []


print(mega_zip(test5, test3))
