# total count average
# This program reads integers until "done", handles errors, and prints stats.

num = 0
tot = 0.0

while True:
    sval = input("Enter a number or 'done' to finish: ")

    if sval == 'done':
        break

    try:
        value = float(sval)
        num = num + 1
        tot = tot + value
    except ValueError:
        print("Invalid input")
        continue

if num > 0:
    print("\nResults from your entries:")
    print("Total:", tot)
    print("Count:", num)
    print("Average:", tot / num)
else:
    print("No numbers were entered.")