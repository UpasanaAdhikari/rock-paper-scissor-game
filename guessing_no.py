import random

count = 0
x = random.randint(2, 100)

while True:
    try:
        y = int(input("Guess a number from 2 to 100: "))
        
        if y < 2 or y > 100:
            print("Please guess a number within the range 2 to 100.")
            continue

        count += 1

        if y > x:
            print("Your guessed number is high.")
        elif y < x:
            print("Your guessed number is low.")
        else:
            print("Your guessed number is correct.")
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

print(f'You have guessed {count} times.')