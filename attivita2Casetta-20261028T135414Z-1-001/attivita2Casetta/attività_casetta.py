import turtle #importo la libreria turtle

#con questo comando metto un'immagine precedentemente scaricata come sfondo
screen= turtle.Screen()
screen.bgpic("sfondoprato.gif")

#scelgo la larghezza della penna
turtle.pensize(3)

#alzo la penna
turtle.penup()

#mi sposto alle cordinate tra parentesi
turtle.goto(-150,-390)

#abbasso la penna
turtle.pendown()

#scelgo i colori
colors=("black","blue","black","purple")

#scelgo il colore interno
turtle.fillcolor("pink")
turtle.begin_fill()

#faccio un ciclo for per disegnare il quadrato
for color in colors:
    turtle.pencolor(color)
    turtle.forward(300)
    turtle.left(90)

#finisco di colorare l'interno
turtle.end_fill()

turtle.penup()
turtle.goto( -150,-90)
turtle.pendown()
colors2=("black","black","white")

turtle.fillcolor("lightgreen")
turtle.begin_fill()
for color2 in colors2:
    turtle.pencolor(color2)
    turtle.forward(300)
    turtle.left(120)
turtle.end_fill()


turtle.penup()
turtle.goto(35,-390)
turtle.pendown()

#scelgo il colore della penna
turtle.pencolor("black")

turtle.fillcolor("orange")
turtle.begin_fill()
for i in range(2):
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
turtle.end_fill()










'''
turtle.pencolor("black")
turtle.penup()
turtle.goto(-100,-200)
turtle.pendown()
turtle.fillcolor("lightblue")
turtle.begin_fill()
for el in range(4):
    turtle.forward(60)
    turtle.left(90)
turtle.end_fill()
'''

 