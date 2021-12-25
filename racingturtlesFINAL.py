# 1.  import the modules

import turtle
import random
import time


def start_line (x, y):
    start_line = turtle.Turtle()
    start_line.penup()
    start_line.setpos(x, y)
    start_line.pendown()
    start_line.right(90)
    start_line.forward(2*y)


def set_turtle_at_line(myturtle, color, x, y):
    myturtle.shape("turtle")
    myturtle.penup()
    myturtle.color(color)
    myturtle.setpos(x, y)


def ready_set_go(myturtle, text):
    myturtle.write(text, align="Center", font=("Open Sans Condensed", 40, "normal"))
    time.sleep(1)
    myturtle.clear()


def place_turtle(myturtle, x, y):
    if x < 250:
        myturtle.setpos(x, y)
        x = x + random.randint( 0 , 10)
        return x


def main():
    wn = turtle.Screen()       # Create a screen
    wn.bgcolor('lightblue')

    # start line is at x=250
    # end line is at x = 250
    # call start_line function

    start_line(-250, 200)
    start_line(250, 200)

    # setting up the turtles at the start line
    white = turtle.Turtle()
    set_turtle_at_line(white, "white", -270, 200)
    red = turtle.Turtle()
    set_turtle_at_line(red, "red", -270, 150)
    brown = turtle.Turtle()
    set_turtle_at_line(brown, "brown", -270, 100)
    orange = turtle.Turtle()
    set_turtle_at_line(orange, "orange", -270, 50)
    yellow = turtle.Turtle()
    set_turtle_at_line(yellow, "yellow", -270, 0)
    green = turtle.Turtle()
    set_turtle_at_line(green, "dark green", -270, -50)
    blue = turtle.Turtle()
    set_turtle_at_line(blue, "blue", -270, -100)
    purple = turtle.Turtle()
    set_turtle_at_line(purple, "purple", -270, -150)

    # Ready Set Go
    go_turtle = turtle.Turtle()
    go_turtle.penup()
    go_turtle.color("black")
    go_turtle.setpos(0, 0)
    go_turtle.pendown()

    ready_set_go(go_turtle, "READY...")
    ready_set_go(go_turtle, "SET...")
    ready_set_go(go_turtle, "GO!!")

    # Lets Race
    xwhite = -270
    xred = -270
    xbrown = -270
    xorange = -270
    xyellow = -270
    xgreen = -270
    xblue = -270
    xpurple = -270

    while xwhite < 250 and xred < 250 and xbrown < 250 and xorange < 250 \
            and xyellow < 250 and xgreen < 250 and  xblue < 250 and xpurple < 250:
        xwhite = place_turtle(white , xwhite , 200)
        xred = place_turtle(red , xred , 150)
        xbrown = place_turtle(brown , xbrown , 100)
        xorange = place_turtle(orange, xorange, 50)
        xyellow = place_turtle(yellow, xyellow, 0)
        xgreen = place_turtle(green, xgreen, -50)
        xblue = place_turtle(blue, xblue, -100)
        xpurple = place_turtle(purple, xpurple, -150)

    winner = turtle.Turtle()
    winner.color("white")
    winning_color = "White won!"
    winningxvalue = xwhite

    if xbrown>winningxvalue:
        winner.color("brown")
        winning_color = "Brown won!"
        winningxvalue = xbrown
    if xred>winningxvalue:
        winner.color("red")
        winning_color = "Red won!"
        winningxvalue = xred
    if xorange>winningxvalue:
        winner.color("orange")
        winning_color = "Orange won!"
        winningxvalue = xorange
    if xyellow>winningxvalue:
        winner.color("yellow")
        winning_color = "Yellow won!"
        winningxvalue = xyellow
    if xgreen>winningxvalue:
        winner.color("dark green")
        winning_color = "Green won!"
        winningxvalue = xgreen
    if xblue>winningxvalue:
        winner.color("blue")
        winning_color = "Blue won!"
        winningxvalue = xblue
    if xpurple>winningxvalue:
        winner.color("purple")
        winning_color = "Purple won!"
        winningxvalue = xpurple

    winner.write(winning_color, align="Center", font=("Open Sans Condensed", 40, "normal"))

    wn.exitonclick()


main()
