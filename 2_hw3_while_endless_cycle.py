while True:
    user_say = input("Say something:")
    if user_say == "Bye":
        print('Oh, bye')
        break
    else:
        print('You are {}'.format(user_say))
        