def day4():
    import turtle

    # 1
    # Forward and Back
    turtle.forward(100)
    turtle.back(100)

    # Left and right
    turtle.right(90)
    turtle.left(90)

    # Change speed
    turtle.speed(2)
    turtle.forward(100)
    turtle.speed(1)
    turtle.back(100)

    # Pen up and down
    turtle.right(90)
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
    turtle.forward(50)

    # Pensize
    turtle.pensize(10)
    turtle.forward(100)
    turtle.pensize(1)
    turtle.back(100)


    # https://docs.python.org/3/library/turtle.html

    # Challenge: Draw a box
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)

    # Challenge: Letter of your name (draws an E)
    turtle.forward(50)
    turtle.back(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.back(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)

day4()