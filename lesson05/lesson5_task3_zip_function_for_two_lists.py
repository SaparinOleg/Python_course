def my_zip(list_one, list_two):

    if not list_one or not list_two:
        return []

    if len(list_one) > len(list_two):
        length_difference = len(list_one) - len(list_two)
        list_one = list_one[:-length_difference]

    if len(list_one) < len(list_two):
        length_difference = len(list_two) - len(list_one)
        list_two = list_two[:-length_difference]

    result_list = []

    for i in range(len(list_one)):
        result_list.append((list_one[i], list_two[i]))
    return result_list


test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
test3 = [1, 2, 3, 4, 5]
test4 = ['a', 'b', 'c', 'd', 'e', 'f']
test5 = [True, False, True, False, True, False, False]


print(my_zip(test2, test5))
