from chessBoard import *



# notes

"""
long delayed yet very necessary to-do list

- plan: keep squareand pieces
- position is a tuple as such: (rank, file)
- player class eventually needed
- game class eventually needed
- work to bring code to a state that can be improved upon, rather than starting various functionalities that rely on other functionalities that are still work in progresses

chess board
|
| 
V
list of square
|
|
V
they can be empty, or they can hold actually chess pieces



"""

# make each piece an object? pros: oop! cons: updating the board and then telling each piece that the board is updated
# indexing pattern [y][x]
# for the for loops, do y outside x inside
# use a tuple to store file and rank (pos, file is x and letters, rank is y and numbers)



##########################################################################################################


fish = Board()
fish.print_board()


