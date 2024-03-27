import turtle

flo = turtle.Turtle()
flo.shape('turtle')
flo.color("Black")

#Method to draw letter N
def N(n):

    n.penup()
    n.goto(-225, 0)
    n.pendown()

    n.left(90)
    n.forward(100)

    n.goto(-175, 0)

    n.forward(100)

    n.penup()

N(flo)

#Method to draw the letter A
def A(a):

    a.penup()
    a.goto(-150,0)
    
    a.pendown()
    a.goto(-125, 100)
    
    a.goto(-100,0)

    a.penup()

    a.goto(-138,50)
    a.pendown()
    a.goto(-112,50)

    a.penup()

A(flo)

#Method to draw the letter T
def T(t):

    t.penup()

    t.goto(-50,0)

    t.pendown()

    t.forward(100)

    t.goto(-100,100)
    t.goto(0,100)

    t.penup()

T(flo)

#Method to draw the letter H
def H(h):

    h.penup()

    h.goto(25,0)

    h.pendown()

    h.left(90)

    h.goto(25,100)

    h.goto(25,50)

    h.right(90)

    h.goto(75,50)

    h.left(90)

    h.goto(75,100)

    h.left(360)

    h.goto(75,0)

    h.penup()

H(flo)

#Method for second A
def AA(aa):

    aa.penup()
    aa.goto(100,0)
    
    aa.pendown()
    aa.goto(125, 100)
    
    aa.goto(150,0)

    aa.penup()

    aa.goto(138,50)
    aa.pendown()
    aa.goto(112,50)

    aa.penup()

AA(flo)

#Method for second N
def NN(nn):

    nn.penup()
    nn.goto(175, 0)
    nn.pendown()

    nn.left(270)
    nn.forward(100)

    nn.goto(225, 0)

    nn.forward(100)

    nn.penup()
   
NN(flo)

#This method draws an exclamation point !
def exclamationPoint(e):

    e.penup()

    e.goto(250,0)

    e.pendown()

    #Makes a small square
    for i in range(4):

        e.forward(10)
        e.right(90)

    e.penup()

    e.goto(250,20)

    e.pendown()

    #makes a rectangle
    for i in range(2):

        e.forward(80)
        e.right(90)
        e.forward(10)
        e.right(90)
    

exclamationPoint(flo)
    

    
    

    
