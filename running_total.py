total = 0

while True:
    number = int(input("Enter a number to add, or 0 to stop: "))
    if number == 0:
        break
    total = total + number

print("Total:", total)

