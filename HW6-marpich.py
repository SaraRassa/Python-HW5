import turtle
T=turtle.Pen()
T.shape("turtle")
turtle.bgcolor("white")

i=0
j=0
n=0

while i < 10:
    n=106+n
    T.left(180-((((i+3-2)*180)/(i+3))/2))
    
    while j <= i+2:
        T.width(1.5)
        T.pencolor('blue')
        
        T.forward(n/(i+3))
        T.left(180-(((i+3-2)*180)/(i+3)))
        j= 1+j
    T.penup()
    T.right(180-(((i+3-2)*180)/(i+3)))
    T.right((((i+3-2)*180)/(i+3))/2)
    T.forward(15)
    T.pendown()
    j=0
    i=1+i
