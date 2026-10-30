import turtle  # importiamo la libreria turtle

# Funzione per disegnare un quadrato
def draw_square(t):
    colors = ["red", "blue", "green", "orange"]  # lista di colori
    t.pensize(5)  # grandezza della penna
    t.fillcolor("pink")  # riempimento colore
    t.begin_fill()
    for color in colors:
        t.pencolor(color)
        t.forward(100)
        t.left(90)
    t.end_fill()  # fine riempimento

# Funzione per disegnare un triangolo equilatero
def draw_triangle(t):
    colors = ["red", "blue", "green"]  # lista di colori
    t.pensize(5)
    t.fillcolor("pink")
    t.begin_fill()
    for color in colors:
        t.pencolor(color)
        t.forward(100)
        t.left(120)
    t.end_fill()  # fine riempimento

# Funzione per disegnare un pentagono
def draw_hexagon(t):
    colors = ["red", "blue", "green", "red", "blue", "green"]  # lista di colori
    t.pensize(5)
    t.fillcolor("pink")
    t.begin_fill()
    for color in colors:
        t.pencolor(color)
        t.forward(100)
        t.left(60)
    t.end_fill()  # fine riempimento

# Funzione per disegnare un ottagono
def draw_octagon(t):
    colors = ["red", "blue", "green", "red", "blue", "green", "blue", "red"]  # lista di colori
    t.pensize(5)
    t.fillcolor("pink")
    t.begin_fill()
    for color in colors:
        t.pencolor(color)
        t.forward(100)
        t.left(45)
    t.end_fill()  # fine riempimento

# Funzione per disegnare una serie di cerchi
def draw_circles(t):
    colors = ["red", "blue", "green", "orange"]  # ogni colore = un cerchio
    t.speed(0)
    t.pensize(2)
    for i in range(9):
        for color in colors:
            t.pencolor(color)
            t.circle(85)
            t.left(10)

# Creiamo la tartaruga
t = turtle.Turtle()

# Disegniamo tutte le figure chiamando le funzioni
# Disegniamo il quadrato
draw_square(t)

# Spostiamo la tartaruga
t.penup()
t.forward(200)
t.pendown()

# Disegniamo il triangolo
draw_triangle(t)

# Spostiamo la tartaruga
t.penup()
t.forward(-400)
t.pendown()

# Disegniamo il pentagono
draw_hexagon(t)

# Spostiamo la tartaruga
t.penup()
t.right(90)
t.forward(150)
t.pendown()

# Disegniamo l'ottagono
draw_octagon(t)

# Spostiamo la tartaruga
t.penup()
t.goto(300, -200)
t.pendown()

# Disegniamo i cerchi
draw_circles(t)

#nascondiamo la tartaruga
t.hideturtle()

#esci schiacciando sull’immagine
turtle.exitonclick()