import numpy as np
from square import Square

class Grid(object):
	def __init__(self, clues):
		self.clues = clues
		self.width = len(clues)
		self.grid = []
		for i in range(self.width):
			temp_row = []
			for j in range(self.width):
				temp_row.append(Square(clues[i][j]))
			self.grid.append(temp_row)

	def find_diag_threes(self):
		for i in range(self.width - 1):
			print("Starting work on row", i)
			for j in range(self.width - 1):
				print(self.grid[i][j].clue, self.grid[i+1][j+1].clue)
				if (self.grid[i][j].clue == 3) and (self.grid[i+1][j+1].clue == 3):
					print("Diagonal 3's found!")
					self.shade_left(i, j)
					self.shade_top(i, j)
					self.shade_right(i + 1, j + 1)
					self.shade_bottom(i + 1, j + 1)
			for j in range(1, self.width):
				print(self.grid[i][j].clue, self.grid[i+1][j-1].clue)
				if (self.grid[i][j].clue == 3) and (self.grid[i+1][j-1].clue == 3):
					print("Diagonal 3's found!")
					self.shade_top(i, j)
					self.shade_right(i, j)
					self.shade_left(i+1, j-1)
					self.shade_bottom(i+1, j-1)

	def shade_left(self, row, col):
		self.grid[row][col].shade_left()
		if col != 0:
			self.grid[row][col - 1].shade_right()

	def shade_right(self, row, col):
		self.grid[row][col].shade_right()
		if col != self.width - 1:
			self.grid[row][col + 1].shade_left()

	def shade_top(self, row, col):
		self.grid[row][col].shade_top()
		if row != 0:
			self.grid[row - 1][col].shade_bottom()

	def shade_bottom(self, row, col):
		self.grid[row][col].shade_bottom()
		if row != self.width - 1:
			self.grid[row + 1][col].shade_top()