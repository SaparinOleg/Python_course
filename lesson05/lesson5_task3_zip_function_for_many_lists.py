def ultimate_zip(*args):
    if not args:
        return []

    incoming_lists = list(args)
    list_length = len(incoming_lists[0])
    for i in range(1, len(incoming_lists)):
        if len(incoming_lists[i - 1]) > len(incoming_lists[i]):
            list_length = len(incoming_lists[i])

    for i in range(len(incoming_lists)):
        if len(incoming_lists[i]) > list_length:
            incoming_lists[i] = incoming_lists[i][:-(len(incoming_lists[i]) - list_length)]

    result_list = []
    future_tuple = []

    for i in range(list_length):
        for j in range(len(incoming_lists)):
            future_tuple.append(incoming_lists[j][i])

        result_list.append(tuple(future_tuple))
        future_tuple.clear()

    return result_list


test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
test3 = [1, 2, 3, 4, 5]
test4 = ['a', 'b', 'c', 'd', 'e', 'f']
test5 = [True, False, True, False, True, False, False]


print(ultimate_zip(test1, test5, test2, test3))
