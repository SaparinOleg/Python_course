print('This is an arsy-versy program:')

"""
import sys
file_content = ""
filename = sys.argv[0]

with open(filename, 'r') as f:
    for line in f:
        file_content += line
for i in file_content[::-1]:
    print(i, end='')
"""

with open("Lesson3_Task2.py", 'r') as file:
    print(file.read()[::-1])

input()
