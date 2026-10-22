def playback_speed():
    user_input = input("What do you want to say? ")
    slowed_input = user_input.replace(" ", "...")
    print(slowed_input)


playback_speed()