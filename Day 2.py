def day2():
    # 1
    name = input("Enter your name: ")
    if name == "Lydia":
        print("Hello Lydia!\n")
    else:
        print("You are not Lydia, :(\n")

    num = 8
    if num < 3:
        string = "Your number is smaller than three"
    elif num > 7:
        string = "Your number is bigger than seven."
    else:
        string = "Your number is inbetween three and seven."

    print(string+"\n")

    # 2
    # number = input("Enter a number: ")
    # newNumber = number + 2
    # Why doesn't this work?

    number = input("Enter a number: ")
    newNumber = int(number) + 2

    string2 = str(8) + "hello"

    print(newNumber)
    print(string2+"\n")

    # Challenge
    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter another integer: "))
    sum = num1 + num2
    print("The sum of "+str(num1)+" and "+str(num2)+" is "+str(sum))

day2()