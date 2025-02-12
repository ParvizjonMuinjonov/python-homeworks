numbers = [2,3,5,7, 10, 45, 85]

odd_numbers = []

odd_numbers.extend(x for x in numbers if x % 2)
print(odd_numbers)