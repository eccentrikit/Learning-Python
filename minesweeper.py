import random

class Minesweeper:
  def setDifficulty(self, difficulty):
    if difficulty == 0:
      self.rows = 3
      self.columns = 3
      self.mines = 2
    if difficulty == 1:
      self.rows = 9
      self.columns = 9
      self.mines = 10
    elif difficulty == 2:
      self.rows = 16
      self.columns = 16
      self.mines = 40
    elif difficulty == 3:
      self.rows = 30
      self.columns = 16
      self.mines = 99
      
  def generateBoard(self):
    self.mineBoard = [[0 for _ in range(self.rows)] for _ in range(self.columns)]
    for i in range(self.mines):
      x, y = self.createBomb()
      for sx, sy in self.getValidSpaces(x, y):
        if self.mineBoard[sy][sx] != "X":
          self.mineBoard[sy][sx] += 1

  def createBomb(self):
    x = random.randint(0, self.columns - 1)
    y = random.randint(0, self.rows - 1)
    if (self.mineBoard[y][x] != "X"):
      self.mineBoard[y][x] = "X"
      return x, y
    else:
      return self.createBomb()

  def generatePlayerBoard(self):
    self.playerBoard = [["-" for _ in range(self.rows)] for _ in range(self.columns)]
    
  def displayBoard(self, board):
      print("  " + " ".join(str(i + 1) for i in range(self.rows)))
      print("  " + "="*self.columns*2)
      for idx, row in enumerate(board):
        print(str(idx + 1) + "|" + " ".join(str(cell) for cell in row))
        print("")

  def getValidSpaces(self, x, y):
    spaces = [(x + 1, y), (x + 1, y + 1), (x, y + 1), (x - 1, y + 1),
                (x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]
    return list(filter(lambda s: s[0] >= 0 and s[0] <= self.rows - 1 
                    and s[1] >= 0 and s[1] <= self.columns - 1, spaces))
      
  def checkSpace(self, x, y):
    if (self.mineBoard[y][x] == 0):
      self.playerBoard[y][x] = " "
      for space in self.getValidSpaces(x, y):
        if self.playerBoard[space[1]][space[0]] != " ":
          self.checkSpace(space[0], space[1])
    else:
      self.playerBoard[y][x] = self.mineBoard[y][x]
      return
    
  def flagSpace(self, x, y):
    if self.playerBoard[y][x] == "-":
      self.playerBoard[y][x] = "F"
    elif self.playerBoard[y][x] == "F":
      self.playerBoard[y][x] = "-"

  def checkWin(self):
    empty = sum(x.count("-") for x in self.playerBoard)
    flagged = sum(x.count("F") for x in self.playerBoard)
    return empty + flagged == self.mines
  
  def getInput(self):
    while True: # infinite loop while getting valid input
      try: 
        coords = input(f"Enter coordinates ({self.rows} {self.columns}): ")
        coords = coords.split(" ")
        if coords[0].lower() == "f":
          x, y = list(map(lambda c: int(c) - 1, coords[1:))
          self.flagSpace(x, y)
        else:
          x, y = list(map(lambda c: int(c) - 1, coords))
          if (self.mineBoard[y][x] == "X"):
            print("Game Over!")
            self.running = False
            self.playerBoard = self.mineBoard
          else:
            self.checkSpace(x, y)
        self.displayBoard(self.playerBoard)
        break # break out of infinite loop
      except:
        pass

  def start(self, difficulty):
    self.setDifficulty(1)
    self.generateBoard()
    self.generatePlayerBoard()
    self.displayBoard(self.mineBoard)
    score = 0
    self.running = True
    while self.running:
      if not self.checkWin():
          self.getInput()
          score += 1
      else:
          print("Winner!")
          break
      print("Score: ", score)

game = Minesweeper()
game.start(1)
