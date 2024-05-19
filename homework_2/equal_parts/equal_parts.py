chars = input("sequence of characters: ")
sequence = chars.split(',')
number_chars = len(sequence)//2

print(sequence[:number_chars], sequence[number_chars:])