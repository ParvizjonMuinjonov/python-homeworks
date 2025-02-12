numbers = [2,3,5,7, 10, 45, 85]

even_numbers = []

even_numbers.extend(x for x in numbers if x % 2 == 0)
print(even_numbers)
