from helpers import next_file

"""
Chess Piece Classes
- A class whose instances encompass the general idea of a chess piece
- Information relating to the chess piece is stored through: 
  ~ color - a string to denote the color of the piece:
    w - white piece
    b - black piece
  ~ state - an integer that ranges from 0-6 that identifies the type of piece that the chess piece is:
    Numerical State Representation
    1 - king
    2 - queen
    3 - rook
    4 - bishop
    5 - knight
    6 - pawn
  ~ pos - a tuple that holds the file and rank of the chess piece
  ~ possible_pos - a list of tuples that are the possible positions that the piece can move
"""
class ChessPiece:
  def __init__(self, color, state, pos):
    self.color = color
    self.state = state
    self.pos = pos
    self.pos_poss = []
    self.update_poss_pos() # as soon as chess piece instantiated, update_poss_pos immediately run
    
  # helper function to check the list of possible positions and remove any that are out of index
  def check_poss_pos(self):
    new_poss_pos = []
    
    for i in range(len(self.poss_pos)):
      
      curr_poss_file = self.poss_pos[i][0]
      curr_poss_rank = self.poss_pos[i][1]
      
      if (not (curr_poss_file == "n" or curr_poss_rank > 8 or curr_poss_rank < 1)):
        new_poss_pos.append(self.poss_pos[i])
        
    self.poss_pos = new_poss_pos
    
  # uniquely implemented in each child class
  def update_poss_pos(self):
      pass
        
"""
Various Specific Chess Piece Classes 
- All of these classes inherit the inherent characteristics of a chess piece
- The main difference between them are how they fill up poss_pos, a list of the tuples of the possible positions they could move on
"""
class King(ChessPiece):
  def __init__(self, color, state, pos):
    super().__init__(color, state, pos)

  def printKing(self):
    print("PRINT KINGJ")
  
  def update_poss_pos(self):
    file = self.pos[0]
    rank = self.pos[1]

    file_right = next_file(file, 1)
    file_left = next_file(file, -1)
    
    rank_up = rank + 1
    rank_down = rank - 1
    
    self.poss_pos = [(file_right, rank_up), (file_right, rank), (file_right, rank_down), (file_left, rank_up), (file_left, rank), (file_left, rank_down), (file, rank_up), (file, rank_down)]
    
    self.check_poss_pos()
    #print(self.poss_pos) to debug how check_poss_pos performs
  