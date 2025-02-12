numbers = [1, 4, 6, 6, 86, 34, 464, 25, 20, 95, 27, 95, 56]

even_numbers = 0

for num in numbers:
    if num % 2 == 0:
        even_numbers += 1
print(even_numbers)