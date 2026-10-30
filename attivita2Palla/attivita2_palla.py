# ============================================================
#  ATTIVITÀ 2 - LA PALLA CHE RIMBALZA (mini-Pong)
# ============================================================
#  Obiettivo: completa le 4 regole del rimbalzo.
#  Cerca i commenti "TODO" e scrivi il codice al posto giusto.
#
#  Aiuto: per ogni TODO ti serve una sola istruzione, per esempio
#      
# ============================================================

import turtle

# --- gioco
schermo = turtle.Screen()
schermo.setup(600, 400)
schermo.title("La palla che rimbalza")
schermo.bgcolor("black")

# tracer(0) dice a turtle di non disegnare subito:
# lo schermo si aggiorna solo quando chiamiamo schermo.update().
# Serve per far muovere la palla in modo fluido.
schermo.tracer(0)

# --- La palla
palla = turtle.Turtle()
palla.shape("circle")
palla.color("yellow")
palla.penup()          # la palla non lascia una scia dietro di sé

# --- Lo stato del gioco dx e dy sono la velocità: quanti pixel la palla si sposta
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

    # TODO 1 - Rimbalzo sul muro DESTRO
    # Se x supera LIMITE_X, la palla deve tornare indietro.
    # Scrivi un if che cambia il segno di dx.
    #
    #
    if x>LIMITE_X:
        dx=-dx

    # TODO 2 - Rimbalzo sul muro SINISTRO
    # Se x è più piccolo di -LIMITE_X, la palla deve tornare indietro.
    # Scrivi un if che cambia il segno di dx.
    #
    #


    # TODO 3 - Rimbalzo sul muro IN ALTO
    # Se y supera LIMITE_Y, la palla deve tornare indietro.
    # Scrivi un if che cambia il segno di dy.
    #
    #

    if(y>LIMITE_Y):
        dy = -dy

    # TODO 4 - Rimbalzo sul muro IN BASSO
    # Se y è più piccolo di -LIMITE_Y, la palla deve tornare indietro.
    # Scrivi un if che cambia il segno di dy.
    #
    #

    # Sposto la palla e aggiorno lo schermo
    palla.goto(x, y)
    schermo.update()

    # Richiamo muovi() tra 20 millisecondi:
    # è questo il "ciclo" che tiene vivo il gioco.
    schermo.ontimer(muovi, 20)

# ============================================================
#  LIVELLI EXTRA (solo se hai finito prima)
# ============================================================
# LIVELLO 2 - Personalizza
#   - Cambia la velocità: prova dx = 8 e dy = 5. Cosa noti?
#   - Cambia il colore: palla.color("cyan")
#   - Rendi la palla più grande: palla.shapesize(2)
#   - Prova a scrivere dx = 0: cosa succede? Perché?
#
# LIVELLO 3 - Scia
#   - Togli il cancelletto dalla riga "palla.pendown()" qui sotto
#     e guarda cosa lascia la palla dietro di sé.
# palla.pendown()
#
# LIVELLO 4 - Il gioco completo
#   - Aggiungi una racchetta che segue il mouse e non far cadere
#     la palla. Chiedi al tutor per un aiuto!
# ============================================================

# --- Avvio --------------------------------------------------
muovi()
schermo.mainloop()      # tiene la finestra aperta
