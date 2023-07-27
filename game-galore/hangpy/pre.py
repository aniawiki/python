with open('words.txt', 'r') as file:
    words = [line.strip() for line in file]

words = [word for word in words if len(word) > 2]

with open('words2.txt', 'w') as file2:
    file2.write('\n'.join(words))
