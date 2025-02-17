numbers = range(1,int(100000000000000000000000000000000000000000000000000000000000000000000000000000))

def factors():
    a = int(input("Enter a positive integer: "))
    for num in numbers:
        if a % num == 0:
            print(f"{num} is a factor of {a}")
            
factors()
