a = input("Enter your password: ")
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if len(a) < 8:
    print("Your password is too short")

elif not any (x in uppercase_letters for x in a):
    print("Password must contain an uppercase letter")

else:
    print("Password is strong")

