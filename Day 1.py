def d1():
    # 1
    print("Hello World!")
    # print: prints a message on the screen

    # 2
    string1 = "Hello"
    string2 = " World!"
    print(string1+string2)

    # Nifty tricks with strings
    # string3 = "Hello\nWorld!"
    # print(string3)

    # 3
    name = input("Enter your name: ")
    message = "Hello "
    print(message+name)

    # Challenge
    name2 = input("What is your name?\n")
    plans = input(name2 + " that's a very nice name, what are your plans for today?\n")
    print("Well, that sounds like fun " + name2 + ". I hope you have fun " + plans + "-ing.")

d1()