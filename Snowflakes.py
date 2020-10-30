
import turtle   #import turtle lib.

elsa = turtle.Turtle()  #start a canvas for the turtle to walk on

elsa.color('white') #change Turtle color to White

turtle.Screen().bgcolor("black")    #change bg color to Black

def branche():
    i = 1
    while i <= 4:
        e = 1
        while e  < 4:
            elsa.forward(30)
            elsa.backward(30)
            elsa.right(45)
            e += 1
        elsa.left(90)
        elsa.backward(30)
        elsa.left(45)
        i += 1
elsa.right(90)
elsa.forward(90)

j = 1

while j <= 5:
    branche()
    elsa.right(45)
    j += 1

turtle.Screen().exitonclick() #closes canvas on click

'''
j = 1

while j <= 5:
    for i in range(10):
        for i in range(2):      
            elsa.forward(100)   #move the turtle 100px forward
            elsa.right(60)      #rotates the turtle by 60 degrees
            elsa.forward(100)   #moves the turtle 100px forward
            elsa.right(120)     #rotates the turtle by 60 degrees
        elsa.right(36) 
    elsa.
    j += 1


turtle.Screen().exitonclick() #closes canvas on click


for j in range(10):     #iterates 10 times over the for loop
    for i in range(2):      
        elsa.forward(100)   #move the turtle 100px forward
        elsa.right(60)      #rotates the turtle by 60 degrees
        elsa.forward(100)   #moves the turtle 100px forward
        elsa.right(120)     #rotates the turtle by 60 degrees
    elsa.right(36)          #rotates the for loop by 36 degrees,da wir 10 Rauten erstellen und ein Kreis 360° hat, drehen wir die Schildkröte immer um 36° in dieselbe Richtung

turtle.Screen().exitonclick() #closes canvas on click
'''