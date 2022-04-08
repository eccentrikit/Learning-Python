class TicTacToe:
  # setup win conditions
  win_conditions = [
    # horizontal lines
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    # vertical lines
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    # diagonal lines
    [0, 4, 8],
    [2, 4, 6]
  ]
  # populate board with empty spaces
  board = [" " for i in range(9)]
  # start the game at turn 0
  turn = 0

  def display_board(self):
    # iterate over the board with index and value
    for id, space in enumerate(self.board):
      # print each row and ending depending on the index
      # over complicated because I wanted to make it one line
      # ternary operator "(true result) if (condition) else (false result)"
      print(space, end="\n" if id == 8 else "\n-+-+-\n" if id % 3 == 2 else "|")

  # return true if game is continuing
  #   false if game is ending
  def check_end(self):
    if self.check_winner():
      return False
    if self.turn > 8:
      self.display_board()
      print("Cat's game!")
    return not self.turn > 8

  def check_winner(self):
    # check if any win condition matches
    # as long as any iteration is true any() will return true
    if any(self.board[cond[0]] != " " and self.board[cond[0]] == self.board[cond[1]] == self.board[cond[2]] for cond in self.win_conditions):
      game.display_board()
      print(self.get_player() + " has won!")
      return True

  def get_player(self):
    # get player symbol based on the turn number with % (modulus) operator
    return "X" if self.turn % 2 else "O"
  
  def get_input(self):
    self.turn += 1
    # infinite loop until valid input
    while True:
      # try to convert user input to int
      try:
        slot = int(input(f"Enter slot for {self.get_player()}:"))
        # check input is valid slot # and check slot is empty
        if slot > 0 and slot < 10 and self.board[slot - 1] == " ":
          self.board[slot - 1] = self.get_player()
          # break out of the infinite loop
          break
      except:
        # in case converting input to int would have crashed the program
        # except can catch the exception and do something else
        # but in this case we don't care, we'll just do a noop (no operation)
        pass
    
# instantiate new TicTaeToe game
game = TicTacToe()
# begin the game loop
while game.check_end():
  game.display_board()
  game.get_input()
