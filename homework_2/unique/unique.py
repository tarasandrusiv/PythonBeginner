seq = input("sequence of numbers: ")
numbers = [int(num) for num in seq.split(',')]
unique = sorted(set(numbers))

print('Unique list:', unique)
