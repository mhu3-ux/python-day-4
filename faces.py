def convert(text):
    converted_input = text.replace(":)", "🙂").replace(":(", "🙁")
    return converted_input


def main():
    user_input = input("Convert to emojis: ")
    print(convert(user_input))


main()