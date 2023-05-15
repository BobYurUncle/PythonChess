from player import Player
from chessBoard import *

class chessGame:
	def __init__(self):
		self.whitePlayer = new Player()
		self.blackPlayer = new Player()
		self.board = new Board()

	def play_game(self):
		pass


	# to-do, need to check the return value of this (what kind of piece are they choosing?)
	def ask_input(self):
		accept = "deny"
		while not accept ==  "confirm":
			init_loc = input("Choose a piece based on its position: ")
			new_loc = input("Please choose a position to move to: ")
			accept = input("Piece at " + init_loc + " will move to " + new_loc + ". Enter \"confirm\" to confirm or anything else to deny.")
			if not accept == "confirm":
				print("You answered deny\n")

		init_pos = (init_loc[0], init_loc[1])
		new_pos = (new_loc[0], new_loc[1])

		return init_pos, new_pos
print()faskdfj;ljas;l