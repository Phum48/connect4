board = [[" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "]]
p1 = "" #empty string
p2 = ""
samename = False
while not samename:
  p1 =input("Please provide player 1 name: ")
  p2 = input("Please provide player 2 name: ")
  if p1 == p2:
    print("Two player cannot have the same name. Please put the names again ")
  else:
    break

rowcol = [0,0,0,0,0,0,0]

def displayboard(board):
  print(" ", board[5][0], "│", board[5][1], "│", board[5][2], "│", board[5][3], "│", board[5][4], "│", board[5][5], "│", board[5][6], "│")
  print(" ───┼───┼───┼───┼───┼───┼───")
  print(" ", board[4][0], "│", board[4][1], "│", board[4][2], "│", board[4][3], "│", board[4][4], "│", board[4][5], "│", board[4][6], "│")
  print(" ───┼───┼───┼───┼───┼───┼───")
  print(" ", board[3][0], "│", board[3][1], "│", board[3][2], "│", board[3][3], "│", board[3][4], "│", board[3][5], "│", board[3][6], "│")
  print(" ───┼───┼───┼───┼───┼───┼───")
  print(" ", board[2][0], "│", board[2][1], "│", board[2][2], "│", board[2][3], "│", board[2][4], "│", board[2][5], "│", board[2][6], "│")
  print(" ───┼───┼───┼───┼───┼───┼───")
  print(" ", board[1][0], "│", board[1][1], "│", board[1][2], "│", board[1][3], "│", board[1][4], "│", board[1][5], "│", board[1][6], "│")
  print(" ───┼───┼───┼───┼───┼───┼───")
  print(" ", board[0][0], "│", board[0][1], "│", board[0][2], "│", board[0][3], "│", board[0][4], "│", board[0][5], "│", board[0][6], "│")
  print("")
displayboard(board)
def initialisedboard():
  print("Hello, and welcome to the connect 4 game\nthere will be two player to play against\n welcome", p1, "and", p2)
  '''note: i will make a grid that not show the number 1-42 cuz trying to reduce the line being used'''
  print(" ", "1", "│", "2", "│", "3", "|", "4", "│", "5", "│", "6", "│", "7") 
  print(" ───┼───┼───┼───┼───┼───┼───")
  print(" ", " ", "│", " ", "│", " ", "|", " ", "│", " ", "│", " ", "│", " ") 
  print(" ───┼───┼───┼───┼───┼───┼───")
  print(" ", " ", "│", " ", "│", " ", "|", " ", "│", " ", "│", " ", "│", " ") 
  print(" ───┼───┼───┼───┼───┼───┼───")
  print(" ", " ", "│", " ", "│", " ", "|", " ", "│", " ", "│", " ", "│", " ") 
  print(" ───┼───┼───┼───┼───┼───┼───")
  print(" ", " ", "│", " ", "│", " ", "|", " ", "│", " ", "│", " ", "│", " ") 
  print(" ───┼───┼───┼───┼───┼───┼───")
  print(" ", " ", "│", " ", "│", " ", "|", " ", "│", " ", "│", " ", "│", " ") 
  print(" ───┼───┼───┼───┼───┼───┼───")
initialisedboard()
def check_win(player):
  for i in range(4): #horizontal win (column)
    for k in range(6): #row
        if board[k][i] == player and board[k][i + 1] == player and board[k][i + 2] == player and board[k][i + 3] == player:
          print (f'{player} has won')
          return True 
#looping through column (below)
  for i in range(7): #vertical win (column)
    for k in range(3): #row
        if board[k][i] == player and board[k + 1][i] == player and board[k + 2][i] == player and board[k + 3][i] == player:
          print (f'{player} has won')
          return True 
#doing digonal check 
  for i in range(4): #column
    for k in range(3): #row
      if board[k][i] == player and board[k + 1][i + 1] == player and board[k + 2][i + 2] == player and board[k + 3][i + 3] == player: #checking row by row and column by column by increase by 1 2 and 3
        print (f'{player} has won')
        return True
  #reverse diagonal check
  for i in range(4): #column
    for k in range(3,6): #row
      if board[k][i] == player and board[k - 1][i + 1] == player and board[k - 2][i + 2] == player and board[k - 3][i + 3] == player: #checking row by row and column by column by increase by 1 2 and 3
        print (f'{player} has won')
        return True
  return False
def ask4inp(player):
  correctinp = False
  x = 0 #count
  while not correctinp:
    try: #it will try something first IF it is wrong input, it will catch and pass it to EXCEPT
      x = 0
      x = int(input(f'{player} please make your move '))
    except: #it catches an error input to here
      print("Wrong input")
    if x < 1 or x > 7:
    
      print("Please choose the number again")
    else:
      correctinp = True #if it is false, it will break the loop
  if rowcol[x - 1] == 6:
    print("All the row has been filled")
    correctinp = False
  board[rowcol[x - 1]][x - 1] = player #we normal count 1-7 but in program it is 0-6 so x - 1

  rowcol[x - 1] = rowcol[x - 1] + 1 #row count (every row)


def startgame():
  gamecontinue = False
  currentplayer = p1
  while not gamecontinue:
    for i in range(7):
      if rowcol[i] != 6: #it will check column by column if one of them is not full, it will continue the game
        gamecontinue = False
        break
      if i == 6:
        print("Game over, it is a draw")
        return False       
    ask4inp(currentplayer)
    displayboard(board)
    gamecontinue = check_win(currentplayer)
    if currentplayer == p1:
      currentplayer = p2
    else:
      currentplayer = p1
startgame()  
