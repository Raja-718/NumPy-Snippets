
import numpy as np

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it! Type 'C' to cancel anytime.\n")

# Generate random number between 1 and 100
secret_number = np.random.randint(1, 101)

attempts = 0

while True:
    user_input = input("Enter your guess (or 'C' to cancel): ").strip()

    if user_input.upper() == 'C':
        print("\n❌ Game cancelled. The number was:", secret_number)
        break

    if not user_input.isdigit():
        print("⚠️ Please enter a valid number.")
        continue

    guess = int(user_input)
    attempts += 1

    if guess < 1 or guess > 100:
        print("⚠️ Guess must be between 1 and 100.")
    elif guess < secret_number:
        print("🔻 Too low. Try again.\n")
    elif guess > secret_number:
        print("🔺 Too high. Try again.\n")
    else:
        print(f"\n✅ Congratulations! You guessed it in {attempts} attempts! 🎉")
        break
