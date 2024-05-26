seq = input("sequence of numbers: ")
numbers = [int(num) for num in seq.split(',')]
numbers.sort()
print('Sorted list:', numbers)

