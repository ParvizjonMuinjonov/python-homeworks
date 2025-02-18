first = int(input("Enter a: "))
second = int(input("Enter b: "))

def check(func):
    def wrapper(a, b):
        try:
            print(func(a / b))
        except ZeroDivisionError:
            print("Denominator can't be zero")
    return wrapper

@check

def div(first, b=second):
    return first

div(first, second)

