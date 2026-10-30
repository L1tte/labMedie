#importo il modulo turtle in modo da poter usare le funzioni ad esso associate
import turtle

#con questo comando inserisco come sfondo un'immagine caricata in precedenza
screen= turtle.Screen()
screen.bgpic("sfondoprato.gif")

#scelgo lo spessore della penna
turtle.pensize(3)

#alzo la penna
turtle.penup()

#mi sposto alle coordinate per iniziare la costruzione della casa
turtle.goto(-150,-390)

#abbasso la penna
turtle.pendown()

#decido i colori da utilizzare per le mura esterne della casa
colors=("black","blue","black","purple")

#scelgo il colore interno delle mura e inizio il riempimento
turtle.fillcolor("pink")
turtle.begin_fill()

#questo ciclo disegnerà le mura della casa
for color in colors:
    turtle.pencolor(color)
    turtle.forward(300)
    turtle.left(90)

#finisco il riempimento delle mura della casa
turtle.end_fill()

#mi sposto nella posizione per iniziare a costruire il tetto
turtle.penup()
turtle.goto( -150,-90)
turtle.pendown()

#decido i colori che utilizzerò per la costruzione delle mura esterne del tetto
colors2=("black","black","white")
turtle.pencolor("black")

#decido il colore del tetto e inizio il riempimento dell'area
turtle.fillcolor("lightgreen")
turtle.begin_fill()

#questo ciclo disegnerà il tetto
for color2 in colors2:
    turtle.pencolor(color2)
    turtle.forward(300)
    turtle.left(120)
    
#finisco il riempimento dell'area del tetto
turtle.end_fill()

#mi sposto in basso per disegnare la porta della casa
turtle.penup()
turtle.goto(35,-390)
turtle.pendown()

#scelgo il colore della penna
turtle.pencolor("black")

#decido il colore della porta e inizio il riempimento dell'area della porta
turtle.fillcolor("orange")
turtle.begin_fill()

#questo ciclo disegna le cornici della porta
for i in range(2):
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)

#finisco il riempimento dell'area della porta
turtle.end_fill()



##########
#soluzione



#decido il colore per la cornice della finestra
turtle.pencolor("black")

#mi sposto alla posizione ideale per disegnare la finestra
turtle.penup()
turtle.goto(-100,-200)
turtle.pendown()

#scelgo il colore e inizio il riempimento della finestra
turtle.fillcolor("lightblue")
turtle.begin_fill()

#questo ciclo serve a disegnare la cornice della finestra
for el in range(4):
    turtle.forward(60)
    turtle.left(90)
    
#finisco il riempimento dell'area della finestra
turtle.end_fill()