history = []

while True:
    command = input("Enter a command: ")

    if command == "history":
        number = 1
        for saved_command in history:
            print(str(number) + ". " + saved_command)
            number = number + 1
    elif command == "exit":
        break
    else:
        history.append(command)
        print("Command logged.")

