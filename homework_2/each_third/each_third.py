chars = input("sequence of characters: ")
elements = chars.split(',')
third_elements = elements[2::3]
print('List of each third element:', third_elements)