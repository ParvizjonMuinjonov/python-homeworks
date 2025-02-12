list1 = ["apple", "banana", "mango", "cherry", "grape", "mango", "cherry", "mango"]

a = len(list1)
middle_element = []
if a % 2 == 0:
    b = a // 2
    v = b - 1
    middle_element.extend([v])
else:
    c = a // 2
    g = c + 1
    middle_element.extend([c, g])

print(middle_element)