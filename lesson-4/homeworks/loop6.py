print("Prime numbers between 1 to 100: ")

for num in range(2,101):
    prime_number = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime_number = False
            break

    if prime_number:
        print(num, end= ", ")