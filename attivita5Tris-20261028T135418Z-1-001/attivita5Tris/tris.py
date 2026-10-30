import turtle as t

screen = t.Screen()
screen.title("Gioco del Tris")

def disegno_campo():
   t.penup()
   t.goto(50, -150)
   t.pendown()
   t.goto(50, 150)
   t.penup()
   t.goto(-50, -150)
   t.pendown()
   t.goto(-50, 150)
   t.penup()
   t.goto(-150, 50)
   t.pendown()
   t.goto(150, 50)
   t.penup()
   t.goto(-150, -50)
   t.pendown()
   t.goto(150, -50)

def disegna_cerchio_blu(x, y):
   t.penup()
   t.goto(x, y - 20)
   t.pendown()
   t.color("blue")
   t.circle(20)

def disegna_cerchio_rosso(x, y):
   t.penup()
   t.goto(x, y - 20)
   t.pendown()
   t.color("red")
   t.circle(20)

def controlla_vincitore(board):
   for i in range(3):
       if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
           return board[i][0]
       if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
           return board[0][i]

   if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
       return board[0][0]
   if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
       return board[0][2]

   return None

def giocare():
   board = [["" for _ in range(3)] for _ in range(3)]
   c = 0

   while True:
       if c == 0:
           print("Turno dei cerchi blu!")
           simbolo = "O blu"
           disegna = disegna_cerchio_blu
       else:
           print("Turno dei cerchi rossi!")
           simbolo = "O rosso"
           disegna = disegna_cerchio_rosso

       o_x = int(input("Scrivi la coordinata x (0, 1, 2): "))
       o_y = int(input("Scrivi la coordinata y (0, 1, 2): "))

       if board[o_x][o_y] != "":
           print("Casella già occupata, scegli un'altra casella.")
           continue

       board[o_x][o_y] = simbolo

       match o_x:
           case 0:
               x = -100
           case 1:
               x = 0
           case 2:
               x = 100
       match o_y:
           case 0:
               y = -100
           case 1:
               y = 0
           case 2:
               y = 100


       disegna(x, y)


       vincitore = controlla_vincitore(board)
       if vincitore:
           print(f"{vincitore} ha vinto!")
           break

       c = 1 - c

disegno_campo()
giocare()
screen.exitonclick()



