import turtle


turtle.setup(750, 700)  # metto la finestra a grandezza di 700 pixel x 700 pixel
turtle.speed(0)  # rendo la velocità della tartaruga di 0 in una scala da 0 a 10 (0-veloce, 10-lento)
turtle.hideturtle()  # nascondo la tartaruga, puoi comunque disegnare
turtle.title("LABIRINTO")




def disegno_labirinto(t):  # disegno tutto il labirinto
   t.width(5)  # la grandezza della tartaruga di 5 pixel
   t.penup()
   t.goto(-360, -130)
   t.pendown()
   t.write("Inizio!", font=("Arial", 15, "bold"))
   t.penup()


   t.goto(-20, 310)
   t.pendown()
   t.write("Fine!", font=("Arial", 15, "bold"))
   t.penup()


   t.goto(-300, -300)
   t.pendown()
   t.goto(-300, -200)
   t.goto(-200, -200)
   t.goto(-200, -100)
   t.penup()
   t.goto(-300, -100)
   t.pendown()
   t.goto(-300, 0)
   t.goto(-100, 0)
   t.goto(-200, 0)
   t.goto(-200, 200)
   t.penup()
   t.goto(-300, 0)
   t.pendown()
   t.goto(-300, 300)
   t.goto(-100, 300)
   t.goto(-100, 100)
   t.goto(-100, 200)
   t.goto(100, 200)
   t.goto(0, 200)
   t.goto(0, -100)
   t.goto(-100, -100)
   t.goto(-100, -200)
   t.penup()
   t.goto(0, -100)
   t.pendown()
   t.goto(100, -100)
   t.goto(100, -200)
   t.goto(200, -200)
   t.goto(200, -100)
   t.penup()
   t.goto(0, 300)
   t.pendown()
   t.goto(300, 300)
   t.goto(300, 200)
   t.goto(200, 200)
   t.goto(300, 200)
   t.goto(300, 100)
   t.goto(200, 100)
   t.goto(300, 100)
   t.goto(300, 0)
   t.goto(100, 0)
   t.goto(100, 100)
   t.penup()
   t.goto(300, 0)
   t.pendown()
   t.goto(300, -300)
   t.goto(0, -300)
   t.goto(0, -200)
   t.goto(0, -300)
   t.goto(-300, -300)
   t.penup()




def attivita(t):  # inserisco le diverse attività
   # disegno i quadrati:
   t.penup()
   t.goto(-275, 270)
   t.pendown()
   t.color("magenta")
   t.begin_fill()
   for i in range(4):
       t.forward(50)
       t.right(90)
   t.penup()
   t.goto(-175, -120)
   t.pendown()
   for i in range(4):
       t.forward(50)
       t.right(90)
   t.end_fill()
   t.penup()


   # disegno i triangoli:
   t.goto(25, 170)
   t.pendown()
   t.color("yellow")
   t.begin_fill()
   for i in range(3):
       t.forward(50)
       t.right(120)
   t.penup()
   t.goto(-275, -230)
   t.pendown()
   for i in range(3):
       t.forward(50)
       t.right(120)
   t.end_fill()
   t.penup()


   # disegno i cerchi:
   t.goto(240, 225)
   t.pendown()
   t.color("cyan")
   t.begin_fill()
   t.circle(25)
   t.penup()
   t.goto(150, -80)
   t.pendown()
   t.circle(25)
   t.end_fill()
   t.penup()
   t.color("black")




disegno_labirinto(turtle)  # richiamo la funzione in cui disegno il labirinto disegnando così il labirinto
attivita(turtle)  # richiamo la funzione in cui disegno le attività inserendo così le attività
turtle.width(3)  # modifico la larghezza della tartaruga
turtle.goto(-330, -150)  # imposto il punto d'inizio
turtle.pendown()
turtle.showturtle()  # mostro la tartaruga
turtle.speed(2)
screen = turtle.Screen()
screen.register_shape('snail_1.gif')  # do alla tartaruga la forma dell'immagine
turtle.shape('snail_1.gif')


'''Comandi base:
-turtle.forward(100) muoversi di 100 pixel
-turtle.left(90) gira a sinistra di 90 gradi
-turtle.right(90) gira a destra di 90 gradi


Attività:
-Quadrati: turtle.color("blue") cambia il colore del cursore di blu
-Triangoli: turtle.write("Ciao a tutti!!", move=True, font=("Arial", 14, "normal")) scrivi una frase
-Cerchi: turtle.bgcolor("red") cambia il colore dello sfondo
'''
turtle.forward()#Inserisci di quanti pixel muovere la lumachina
turtle.left()#Inserisci di quanti gradi girare la lumachina
turtle.forward()#Inserisci di quanti pixel muovere la lumachina
# Adesso vai avanti tu:
turtle.exitonclick()
