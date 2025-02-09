word = input("Enter a word: ")

palindrome_check = word[::-1]

if word == palindrome_check:
    print(f"{word} is a palindrome")

else:
    print(f"{word} is not a palindrome")