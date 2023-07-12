import re

with open('Task2 input.txt', 'r') as file_in:
    text = re.sub(r'[^a-zA-Z \n]', '', file_in.read()).lower().split()
print(text)
dict_of_words = dict.fromkeys(text, 1)

text = sorted(text)
for i, word in enumerate(text):
    if i < len(text) - 1:
        if word == text[i + 1]:
            dict_of_words[word] += 1
    else:
        break

dict_of_words = dict(sorted(dict_of_words.items(), key=lambda key: key[1], reverse=True))

# with open('Task2 output.txt', 'w') as file_out:
#     for i in dict_of_words:
#         file_out.write(f'{i}: {dict_of_words[i]}\n')

for i in dict_of_words:
    print(f'{i}: {dict_of_words[i]}')
