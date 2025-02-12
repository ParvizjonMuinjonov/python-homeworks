numbers = [1, 2, 4, 69, 93, 0, 72, 194]
numbers_min = min(numbers)
b = numbers.index(numbers_min)

numbers.pop(b)

numbers_min2 = min(numbers)

print(numbers_min2)