# maximum_minimum
# This script finds the max and min values from user input using a list.
# Create an empty list named numbers to store the numeric inputs
numbers = []

while True :
# Prompt the user to enter a number or the word done
    user_input = input("\n Please enter a number or done to stop: ")

# Check if the user entered done to stop the loop
    if user_input == 'done':
        break

    try:
# Convert the input to a float and add it to the list
        number = float(user_input)
        numbers.append(number)
    except ValueError:
# If the float conversion fails, notify the user and continue
        print("\n Invalid input. Please enter a number or done to stop")

# Check if the list is not empty before calculating min and max
if numbers:
    print("\nMaximum input is ", max(numbers))
    print("\nMinimum input is", min(numbers))
else:
# Inform the user if no numbers were provided
    print("\n!!! No numbers were entered >>>\n")

