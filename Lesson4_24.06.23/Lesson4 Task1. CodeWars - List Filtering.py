# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

# Create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

li = [1, '1', 12, 'zxc', 2, 'abc', '45', 5]
print([num for num in li if not isinstance(num, str)])
