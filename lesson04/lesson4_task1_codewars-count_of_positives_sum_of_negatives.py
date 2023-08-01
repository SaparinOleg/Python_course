# https://www.codewars.com/kata/576bb71bbbcf0951d5000044

# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative
# numbers. 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.

from functools import reduce
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]

print(reduce(lambda acc, number: [(acc[0] + (number > 0)), (acc[1] + number * (number < 0))], arr, [0, 0])) if arr else print([])


"""
positives = 0
negatives = 0
if not arr:
    print([])
else:
    for num in arr:
        if num > 0:
            positives += 1
        else:
            negatives += num

    print(positives, negatives)
"""

"""
positives = 0
negatives = 0
if not arr:
    print([])
else:
    for num in arr:
        positives += 1 * (num > 0)
        negatives += num * (num <= 0)
        
    print(positives, negatives)
"""
