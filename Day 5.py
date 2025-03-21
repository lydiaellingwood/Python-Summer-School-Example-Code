def day5():
    # 1 Review
    import turtle as t
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)

    # 2
    # While loop example
    cats = 0
    while cats < 3:
        cats = cats +1

    print(cats)

    i = 0
    while i > 4:
        t.forward(100)
        t.right(90)
        i += 1

    # for loop example
    for cats in range (3):
        print(cats)

    for i in range (4):
        t.forward(100)
        t.right(90)

    # Hexagons
    i = 0
    while i < 6:
        t.forward(100)
        t.right(60)
        i += 1

    for i in range (6):
        t.forward(100)
        t.right(60)

    # circles
    for i in range (360):
        t.forward(1)
        t.right(1)

    t.circle(50)

    # Challenge
    n = int(input("Enter how many sides you want your polygon to have: "))
    l = input("What sidelength should your polygon have: ")
    for side in range(n):
        t.forward(l)
        t.right(360/n)



day5()