def convert_cel_to_far():
    c = int(input("Enter the temperature in Celsius: "))
    f = c * 9/5 + 32
    
    print(f"{c} Celsius in Farenheit will be: {f:.2f}")

convert_cel_to_far()

def convert_far_to_cel():
    far = int(input("Enter the temperature in Farenheit: "))
    cels = (far - 32) * 5/9
    print(f"{far} Farenheit in Celsius will be: {cels:.2f}")

convert_far_to_cel()
