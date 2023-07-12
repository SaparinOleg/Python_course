import sys

filename = sys.argv[0]

with open(filename, 'r') as f:
    print('Program code:\n')
    for line in f:
        print(line, end="")

"""
with open("Lesson3_Task1.py", 'r') as file:
    print(file.read())
"""

input()
