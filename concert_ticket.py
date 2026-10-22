age = int(input("What is your age? "))

if age < 13:
    print("Child ticket: $8")
elif age >= 65:
    print("Senior ticket: $10")
else:
    print("General admission: $1")
