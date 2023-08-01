# На вход подаётся список чисел. Необходимо вернуть отсортированный список только с уникальными элементами, без повторов

the_list = [10, 2, 2, 56, 2, 56, 11, 555, 41, 666, 666]
the_list = sorted(the_list)

"""
if not the_list:
    print(None)
elif len(the_list) == 1:
    print(the_list[0])
for num in range(len(the_list) - 1, 0, -1):
    if the_list[num] == the_list[num - 1]:
        the_list.pop(num)
"""

# the_list = [the_list[0]] + [the_list[num] for num in range(1, len(the_list), 1) if the_list[num] != the_list[num - 1]]

the_list = sorted(list(set(the_list)))

print(the_list)
