def main():
    c = input("Do you want to play again?")
    loop(c)

def loop(c):
    if c == 'yes':
        print("Go ahead!")
        ask()
    else:
        print("Goodbye! Have fun!")

def ask():
    name = input("What is your name?")
    print("Nice to meet you", name, "!")
    color = input("What is your favorite color?")
    print(color + "!", "That's a nice color")
    food = input("Which is your favorite food?")
    print(food + "!", "yummy!!!")
    main()
ask()
