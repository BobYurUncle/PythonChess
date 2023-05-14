"""
General Helper Functions
"""

# a helper function to return a specific chess piece type given a particular index (ie state)
def create_piece(color, state, position):

  from chessPieces import King # every type of chess piece imported here as to avoid circular import error
  
  # based on the numerical state representations in the chess piece class comments
  piece = ""
  
  if state == 1:
    piece = King(color, state, position)
    
  elif state == 2: # note to self: most of these are as of yet implemented
    #piece = Queen(color, state, position)
    pass
    
  elif state == 3:
    #piece = Rook(color, state, position)
    pass
    
  elif state == 4:
    #piece = Bishop(color, state, position)
    pass
    
  elif state == 5:
    #piece = Knight(color, state, position)
    pass
    
  elif state == 6:
    #piece = Pawn(color, state, position)
    pass
    
  else:
    print("AHHHHH, STATE IS NOT VALID!!!! CHECK WHAT YOU PLUG INTO CREATE PIECE!!!")

  
  return piece


# helper function to progress from an original file value to another file value based on a number
def next_file(file, val):
  
  letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

  # finds the letter in the list and gets its index
  index = ""
  for n in range(len(letters)):
    
    if letters[n] == file:
      index = n

  # note: to find a previous file, val should be a negative number
  possible_index = index + val
  
  if (possible_index > len(letters) - 1) or (possible_index < 0):
    # tells the original function that this file isn't possible
    return "n" 
  
  return letters[possible_index]


# helper function to check if a position is inside a list of possible positions, all positions are in the rank and file system and are held through tuples
def inside_poss_pos(poss_pos, pos):
  
  for n in poss_pos:

    # comparing respective ranks and files of the position from the list of possible positions and the given position
    if n[0] == pos[0] and n[1] == pos[1]:
      return True

  return False


# alternate version of the above helper function, checking if a position is present in list of possible positions but the given position is in the form of x and y
def inside_poss_pos_raw(poss_pos, x, y):
  
  for n in poss_pos:

    poss_pos_x, poss_pos_y = file_rank_indices(n)

    # converting possible position to x and y format and then comparing
    if poss_pos_x == x and poss_pos_y == y:
      return True

  return False
  

# helper function to convert inputs in the form of the traditional chess file and rank into indices that can be used to access values in a two-dimensional list
def file_rank_indices(pos):

  file = pos[0]
  rank = pos[1]
  
  # note: all uppercase letters are converted to lowercase  
  file.lower()

  # converting to x, y coordinates, where (0,0) is the bottom corner
  x = ord(file) - ord("a")
  y = rank - 1

  # checking input
  if x > 7 or x < 0:
    raise Exception("Custom error: get_square() method, file val is erroneous")
    
  elif y > 7 or y < 0:
    raise Exception("Custom error: get_square() methofd, rank val is erroneous")

  # converting to proper indices that work with a two-dimensional list (x already works, y doesn't)
  y = 7 - y
  
  return x, y

# helper formatting function to print a line
def print_line(n=False):
  
  row = ""
  
  if not n == False:
    for i in range(n):
      row += "-"
      
  else:
    for i in range(24):
      row += "-"
      
  print(row)

