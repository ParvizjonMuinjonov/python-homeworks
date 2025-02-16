from random import randint
answer_examples = ["Y", "YES", "y", "yes", "ok"]
a = randint(1, 100)
i = 0
while True:
    guess = int(input("Enter your guess: "))
    if guess > a:
        print("Your guess is too high")
        

    elif guess < a:
        print("Your guess is too low")
        

    else:
        print("Your guess is correct")
        
        break
    i += 1
    print(f"You have {10-i} attempts left")

    if i == 10:
        print(f"Game over! The correct number was {a}")
        answer = input("Do you want to play again?: ").strip()

        if answer not in answer_examples:
            print("Thanks for playing")
            break
        elif answer in answer_examples:
            i = 0






