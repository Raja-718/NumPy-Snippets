import numpy as np

# Define dot representation for numbers 1–6
dot_representation = {
    1: "| * |",
    2: "| * * |",
    3: "| * * * |",
    4: "| * * * * |",
    5: "| * * * * * |",
    6: "| * * * * * * |"
}

# Prompt user to roll or cancel
user_input = input("Press R to roll the dice or C to cancel: ").strip().upper()

if user_input == "R":
    dice = np.random.randint(1, 7)
    print(f"\nYou rolled: {dice}")
    print(dot_representation[dice])
elif user_input == "C":
    print("Cancelled.")
else:
    print("Invalid input. Please press R or C.")
