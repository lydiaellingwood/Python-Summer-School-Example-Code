def day3():
    # 1
    float1 = 0.4
    string = "9.45"
    float2 = float(string)

    # To add
    sum = float1 + float2

    # To subtract
    difference = float1 - float2

    # To multiply
    product = float1*float2

    # To divide
    quotient = float1/float2

    # All of these things also work with integers!

    # Challenge: Make a calculator
    sign = input("Enter the sign of the operator you want to use (+-*/): ")
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    result = ''
    if sign == "+":
        result = num1+num2
    elif sign == "-":
        result = num1-num2
    elif sign == "*":
        result = num1*num2
    elif sign == "/":
        result = num1/num2
    else:
        print("It seems that you did not enter a valid sign")
    print(result)


day3()