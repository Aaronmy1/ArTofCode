import turtle
bob= turtle.Turtle()
bob.shape("turtle")

def square(size):
    for times in range (4):
        bob.forward(size)
        bob.left(90)
        bob.color("blue")
def triangle(size):
    for times in range (3):
        bob.forward(size)
        bob.left(120)
        bob.color("yellow")
def pentagon(size):
    for times in range(5):
        bob.forward(size)
        bob.left(72)
        bob.color("pink")
def hexagon(size):
    for times in range(6):
        bob.forward(size)
        bob.left(60)
        bob.color("purple")
def polygon (side, size, c):
    bob.begin_fill()
    bob.color(c)
    angle=360/side
    for times in range(side):
        bob.forward(size)
        bob.left(angle)
    bob.end_fill()
def comet(size,angle,amt):
    for times in range(amt):
        bob.width(times)
        bob.forward(size)
        bob.left(angle)
        
def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def stair(distance, amount,c, w):
    bob.color(c)
    bob.width(w)
    for times in range(amount):
        bob.forward(distance)
        bob.left(90)
        bob.forward(distance)
        bob.right(90)

def drawsquare( sizeS,sizeC):
    for times in range(4):
        bob.forward(sizeS)
        bob.right(90)
        bob.circle(sizeC)
        
def tree(x,y,side):
    jump(x,y)
    polygon(100,3,"purple")
    bob.forward(25)
    bob.right(90)
    polygon(40,4,"brown")
    bob.left(90)
    
def PLATINUM(x,y,circle):
    bob.speed(0)
    jump(x,y)
    polygon(100,3,"purple")
    bob.forward(25)
    bob.right(90)
    polygon(40,4,"gold")
    bob.left(90)

def STAR(x,y,circle):
    bob.speed(0)
    jump(x,y)
    polygon(100,3,"teal")
    bob.forward(25)
    bob.right(90)
    polygon(40,4,"black")
    bob.left(90)
