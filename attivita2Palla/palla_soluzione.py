# ============================================================
#  ATTIVITÀ 2 - LA PALLA CHE RIMBALZA (mini-Pong)
#  SOLUZIONE
# ============================================================
#  Le 4 regole del rimbalzo sono indicate con "SOLUZIONE".
#  Il resto del programma è identico alla versione degli studenti.
# ============================================================

import turtle

# --- La finestra di gioco -----------------------------------
schermo = turtle.Screen()
schermo.setup(600, 400)
schermo.title("La palla che rimbalza - soluzione")
schermo.bgcolor("black")

# tracer(0) dice a turtle di non disegnare subito:
# lo schermo si aggiorna solo quando chiamiamo schermo.update().
schermo.tracer(0)

# --- La palla -----------------------------------------------
palla = turtle.Turtle()
palla.shape("circle")
palla.color("yellow")
palla.penup()          # la palla non lascia una scia dietro di sé

# --- Lo stato del gioco -------------------------------------
# dx e dy sono la velocità: quanti pixel la palla si sposta
# ad ogni fotogramma, in orizzontale (dx) e in verticale (dy).
dx = 4
dy = 3

# I limiti: la finestra è larga 600 e alta 400, quindi il centro
# è (0, 0) e i muri sono a metà strada.
LIMITE_X = 280         # muro destro e sinistro
LIMITE_Y = 180         # muro in alto e in basso

# --- Le regole del gioco ------------------------------------
def muovi():
    # "global" serve per poter cambiare dx e dy dentro la funzione.
    global dx, dy

    # Calcolo la prossima posizione della palla
    x = palla.xcor() + dx
    y = palla.ycor() + dy

    # SOLUZIONE 1 - Rimbalzo sul muro DESTRO
    if x > LIMITE_X:
        x = LIMITE_X      # riporto la palla sul muro
        dx = -dx          # e cambio direzione

    # SOLUZIONE 2 - Rimbalzo sul muro SINISTRO
    if x < -LIMITE_X:
        x = -LIMITE_X
        dx = -dx

    # SOLUZIONE 3 - Rimbalzo sul muro IN ALTO
    if y > LIMITE_Y:
        y = LIMITE_Y
        dy = -dy

    # SOLUZIONE 4 - Rimbalzo sul muro IN BASSO
    if y < -LIMITE_Y:
        y = -LIMITE_Y
        dy = -dy

    # Sposto la palla e aggiorno lo schermo
    palla.goto(x, y)
    schermo.update()

    # Richiamo muovi() tra 20 millisecondi:
    # è questo il "ciclo" che tiene vivo il gioco.
    schermo.ontimer(muovi, 20)

# --- Bonus (da mostrare solo se c'è tempo) -------------------
# Per accelerare la palla:
#     dx = dx * 1.01
# Per lasciare una scia:
#     palla.pendown()

# --- Avvio --------------------------------------------------
muovi()
schermo.mainloop()      # tiene la finestra aperta
