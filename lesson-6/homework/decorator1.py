first = int(input("Enter a: "))
second = int(input("Enter b: "))

def check(func):
    def wrapper(a, b):
        try:
            return func(a / b)
        except ZeroDivisionError:
            return "Denominator can't be zero"
    return wrapper

@check

def div(result):
    return result

print(div(first, second))

