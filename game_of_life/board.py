import numpy as np
import os, time

from game_params.game_params import *

class Board():
	"""
	usage - b = Board([height, width, list_of_points])
	all args in [] are optional, default values loaded from `game_config.json`
	"""
	def __init__(self, height_param = board_height, width_param = board_height, live_cells = alive_cells):
		"""
		board - 2D boolean board containing info 
		live - marker to be used for showing
		dead - marker to be used for showing
		"""
		self.height = height_param
		self.width = width_param

		if self.height <= 0 or self.width <= 0 :
			raise ValueError("Board dimensions can't be negative")

		if self.height == None or self.width == None:
			raise TypeError("Board dimensions can't be None")

		self.board = np.zeros((self.height, self.width), dtype=bool)
		self.live = live_marker
		self.dead = dead_marker

		for cell in live_cells :
			r,c = cell

			if r > self.height or r < 0 or c > self.width or c < 0 :
				raise IndexError("Alive cells can't be outside board")

			self.board[r][c] = 1

	def step(self):
		"""
		emulates one step of a time for the whole board
		"""

		board_copy = self.board.copy()

		for col in range(self.width):
			for row in range(self.height):
				cell = (row, col)
				neighbor = self.neighbors(cell)

				if self.board[row][col] == 1 :
					if neighbor < 2 :
						# Any live cell with fewer than two live neighbours dies,
						# as if caused by underpopulation.
						board_copy[row][col] = 0

					if neighbor == 2 or neighbor == 3 :
						# Any live cell with two or three live neighbours lives
						# on to the next generation.
						board_copy[row][col] = 1

					if neighbor > 3 :
						# Any live cell with more than three live neighbours dies,
						# as if by overpopulation.
						board_copy[row][col] = 0

				if self.board[row][col] == 0 :
					if neighbor == 3 :
						# Any dead cell with exactly three live neighbours becomes a live cell,
						# as if by reproduction.
						board_copy[row][col] = 1

		self.board = board_copy

	
	def neighbors(self, cell):
		"""
		return - no of alive member around a cell
		"""
		x,y = cell
		num_neighbors = 0

		if self.board[x][(y+1)%self.width] == 1 : num_neighbors += 1
		if self.board[x][(y-1)%self.width] == 1 : num_neighbors += 1
		if self.board[(x+1)%self.height][(y-1)%self.width] == 1 : num_neighbors += 1
		if self.board[(x+1)%self.height][y] == 1 : num_neighbors += 1
		if self.board[(x+1)%self.height][(y+1)%self.width] == 1 : num_neighbors += 1
		if self.board[(x-1)%self.height][(y+1)%self.width] == 1 : num_neighbors += 1
		if self.board[(x-1)%self.height][y] == 1 : num_neighbors += 1
		if self.board[(x-1)%self.height][(y-1)%self.width] == 1 : num_neighbors += 1

		return num_neighbors


	def __str__(self):
		"""
		return - current state of board as a string
		"""

		os.system('clear')
		current_board = ""

		for col in range(self.width):
			for row in range(self.height):
				if self.board[row][col]:
					current_board += self.live
				else : current_board += self.dead
			current_board += '\n'

		return current_board
