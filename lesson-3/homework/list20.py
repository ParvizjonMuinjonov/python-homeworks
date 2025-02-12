numbers = [1, 2, 4, 69, 93, 0, 72, 194]
numbers_max = max(numbers)
b = numbers.index(numbers_max)

numbers.pop(b)

numbers_max2 = max(numbers)

print(numbers_max2)