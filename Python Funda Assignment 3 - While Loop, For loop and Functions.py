# QUESTION 1: WHILE LOOP - NUMBER GUESSING GAME
# ------------------------------------------

import random

print("\n===== NUMBER GUESSING GAME =====")

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Set maximum attempts
attempts = 3

# Start the guessing game
while attempts > 0:

    guess = int(input("Guess the number (between 1 and 10): "))

    # Check whether the guess is within the valid range
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue

    # Check whether the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess > secret_number:
        print("Too high. Try again.")

    else:
        print("Too low. Try again.")

    # Reduce the number of attempts
    attempts -= 1

else:
    print("Better luck next time!")
    print("The correct number was:", secret_number)

# QUESTION 2: FOR LOOP - MULTIPLICATION TABLE
# ------------------------------------------

print("\n===== MULTIPLICATION TABLE GENERATOR =====")

# Get a number from the user
number = int(input("Enter the number for which you want the multiplication table: "))

# Generate multiplication table from 1 to 10
for i in range(1, 11):

    result = number * i

    print(number, "x", i, "=", result)

# QUESTION 3: FUNCTION - BMI CALCULATOR
# ------------------------------------------

print("\n===== BMI CALCULATOR =====")

# Define a function to calculate BMI
def calculate_bmi(weight, height):

    bmi = weight / (height ** 2)

    return bmi


# Get weight and height from the user
weight = float(input("Enter your weight in kg: "))

height = float(input("Enter your height in meters: "))

# Call the function
bmi_result = calculate_bmi(weight, height)

# Display BMI rounded to two decimal places
print(f"Your BMI is: {bmi_result:.2f}")
