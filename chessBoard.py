from chessPieces import *
from helpers import print_line, create_piece, file_rank_indices, inside_poss_pos_raw

"""
Board Class
- A class whose instances represent a board in the game of chess
- Information relating to the chess board is stored through: 
  ~ board - a two-dimensional board used to store the squares of a chess board
"""
class Board:
  def __init__(self):
    self.board = [[],[],[],[],[],[],[],[]]
    self.create_board()


  # DEBUG FUNCTION TO CHECK WHERE A PIECE'S POSS_POS SHOWS UP ON BOARD
  # choose the piece using its position
  def strike_all_pos(self, pos):

    square = self.get_square(pos)
    piece = square.status
    poss_pos = piece.poss_pos
    piece_str = piece.color + str(piece.state)
    
    print_line(60)
    print("This is the possible positions of the piece: " + piece_str)
    print(poss_pos)

    for y in range(8):
      val = " "
      for x in range(8):
        # marking a position as a possible spot, regardless if there's something in the way
        if inside_poss_pos_raw(poss_pos, x, y) == True:
          val += "XX "
        else:
          curr_status = self.board[y][x].check_status()
          if curr_status == False:
            val += "00 "
          else:
            color = curr_status.color
            type = curr_status.state
            val += color + str(type) + " "
      print(val)
    print_line(60)

    
    
  # fills up self.board with a two-dimensional array list
  def create_board(self, empty=False):
    
    # creates an empty 8x8 two-dimensional array list
    for y in range(8):
      for n in range(8):
        self.board[y].append(Square()) # empty squares

    # fills up chess board with default pieces in default positions
    if not empty:

      # kings
      w_king = create_piece("w", 1, ("e", 1))
      b_king = create_piece("b", 1, ("e", 8))
      
      self.set_square(w_king, w_king.pos)
      self.set_square(b_king, b_king.pos)

      """


      lol gotta switch the position and color and state around (parameter ordering is a problem)
      # queens
      create_piece(("d", 1), "w", 2)
      create_piece(("d", 8), "b", 2)

      # rooks
      create_piece(("a", 1), "w", 3)
      create_piece(("h", 1), "w", 3)
      create_piece(("a", 8), "b", 3)
      create_piece(("h", 8), "b", 3)

      # bishops
      create_piece(("c", 1), "w", 4)
      create_piece(("f", 1), "w", 4)
      create_piece(("c", 8), "b", 4)
      create_piece(("f", 8), "b", 4)

      # knight
      create_piece(("b", 1), "w", 5)
      create_piece(("g", 1), "w", 5)
      create_piece(("b", 8), "b", 5)
      create_piece(("g", 8), "b", 5)

      # pawns
      first_eight = ["a", "b", "c", "d", "e", "f", "g", "h"]
      for n in first_eight:
        create_piece((n, 2), "w", 6)
        create_piece((n, 7), "b", 6)
      """

    
  # prints the board
  def print_board(self, format=False): # format = True, there will be a prettier way to print out the board, but that's for later

    print_line()
    
    if not format:
      
      for y in range(8):
        
        val = " "
        
        for x in range(8):
          piece = self.board[y][x].check_status() # board is a 2d list of states
          
          if piece == False:
            val += "00 "
            
          else:
            color = piece.color
            type = piece.state

            val += color + str(type) + " "
        print(val)

    print_line()

        
  # a function to index into the board through the traditional file and rank system of chess
  def get_square(self, pos):

    x, y = file_rank_indices(pos)
    return(self.board[y][x])


  # a function to change the value of a square on the board through the traditional file and rank system of chess
  def set_square(self, piece, pos):

    x, y = file_rank_indices(pos)
    self.board[y][x] = Square(piece)



"""
Square Class
- A class whose instances represent the squares on a chess board
- Information related to each square is stored through: 
  ~ status - what is on a square, can either be a chess piece object or the boolean False, if status is set to False, that square is empty on the board
"""
class Square:
  def __init__(self, status=False):
    
    self.status = status

  def set_status(self, new_status):
    
    self.status = new_status

  def empty_status(self):
    
    self.status = False
  
  def check_status(self):
    
    return self.status 

  # used to individually print a square state
  def print_status(self):
    
    if self.status  == False:
      print("empty square")
      
    else: 
      print(self.status.color + str(self.status.state))